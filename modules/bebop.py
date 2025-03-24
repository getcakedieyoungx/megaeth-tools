from core.web3_client import Web3Client
from eth_account import Account
import random
import asyncio

class BebopExchange:
    def __init__(self, web3_client: Web3Client):
        self.w3 = web3_client
        self.contract_address = self.w3.config['contracts']['bebop']
        
        self.swap_abi = [{
            "inputs": [
                {
                    "internalType": "address",
                    "name": "tokenIn",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "tokenOut",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "amountIn",
                    "type": "uint256"
                }
            ],
            "name": "swap",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }]

    async def swap_tokens(self, private_key: str, token_in: str, token_out: str, amount_in: int):
        contract = self.w3.w3.eth.contract(
            address=self.contract_address,
            abi=self.swap_abi
        )
        
        tx = contract.functions.swap(
            token_in,
            token_out,
            amount_in
        ).build_transaction({
            'from': Account.from_key(private_key).address,
            'value': 0
        })
        
        return await self.w3.send_transaction(private_key, tx)

    async def perform_swaps(self, private_key: str, pairs: list):
        results = []
        for token_in, token_out, amount in pairs:
            try:
                result = await self.swap_tokens(private_key, token_in, token_out, amount)
                results.append((f"{token_in}->{token_out}", result))
                await asyncio.sleep(random.uniform(3, 7))
            except Exception as e:
                results.append((f"{token_in}->{token_out}", str(e)))
        return results