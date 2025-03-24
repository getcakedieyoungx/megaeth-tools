from core.web3_client import Web3Client
from eth_account import Account
import asyncio
import random

class GTEFaucet:
    def __init__(self, web3_client: Web3Client):
        self.w3 = web3_client
        self.contract_address = self.w3.config['contracts']['gte_faucet']
        
        self.abi = [{
            "inputs": [],
            "name": "claimTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }]
        
        self.contract = self.w3.w3.eth.contract(
            address=self.contract_address,
            abi=self.abi
        )

    async def claim_tokens(self, private_key: str):
        tx = self.contract.functions.claimTokens().build_transaction({
            'from': Account.from_key(private_key).address,
            'value': 0
        })
        
        return await self.w3.send_transaction(private_key, tx)