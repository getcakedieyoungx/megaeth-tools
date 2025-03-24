from core.web3_client import Web3Client
from eth_account import Account
import random
import asyncio

class TekoFinance:
    def __init__(self, web3_client: Web3Client):
        self.w3 = web3_client
        self.contracts = self.w3.config['contracts']['teko']
        
        self.mint_abi = [{
            "inputs": [],
            "name": "mint",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }]

    async def mint_token(self, private_key: str, token_type: str):
        if token_type not in self.contracts:
            raise ValueError(f"Invalid token type: {token_type}")
            
        contract = self.w3.w3.eth.contract(
            address=self.contracts[token_type],
            abi=self.mint_abi
        )
        
        tx = contract.functions.mint().build_transaction({
            'from': Account.from_key(private_key).address,
            'value': 0
        })
        
        return await self.w3.send_transaction(private_key, tx)

    async def mint_all(self, private_key: str):
        results = []
        for token in ['tkETH', 'tkUSDC', 'tkWBTC']:
            try:
                result = await self.mint_token(private_key, token)
                results.append((token, result))
                await asyncio.sleep(random.uniform(3, 7))
            except Exception as e:
                results.append((token, str(e)))
        return results