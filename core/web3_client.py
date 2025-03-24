from web3 import Web3, HTTPProvider
from eth_account import Account
import json
import asyncio
import random

class Web3Client:
    def __init__(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f)
        
        self.w3 = Web3(HTTPProvider(self.config['rpc_url']))
        self.chain_id = self.w3.eth.chain_id

    async def send_transaction(self, private_key: str, tx_params: dict):
        account = Account.from_key(private_key)
        
        if 'nonce' not in tx_params:
            tx_params['nonce'] = self.w3.eth.get_transaction_count(account.address)
        
        if 'chainId' not in tx_params:
            tx_params['chainId'] = self.chain_id

        if 'gas' not in tx_params:
            tx_params['gas'] = 3000000

        signed_tx = self.w3.eth.account.sign_transaction(tx_params, private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        await asyncio.sleep(random.uniform(3, 7))
        return await self.w3.eth.wait_for_transaction_receipt(tx_hash)