import asyncio
import json
from core.web3_client import Web3Client
from modules.faucet import GTEFaucet
from modules.cap import CAPApp
from modules.teko import TekoFinance
from modules.bebop import BebopExchange
from modules.gte import GTEExchange

async def main():
    # Load config
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Initialize Web3 client
    web3_client = Web3Client(config)
    
    # Initialize modules
    faucet = GTEFaucet(web3_client)
    cap = CAPApp(web3_client)
    teko = TekoFinance(web3_client)
    bebop = BebopExchange(web3_client)
    gte = GTEExchange(web3_client)
    
    # Get private key from user
    private_key = input("Enter your private key: ")
    
    try:
        # Claim from faucet
        print("\nClaiming from faucet...")
        result = await faucet.claim_tokens(private_key)
        print(f"Faucet claim result: {result}")
        
        # Mint CAP tokens
        print("\nMinting CAP tokens...")
        result = await cap.mint_tokens(private_key)
        print(f"CAP mint result: {result}")
        
        # Mint Teko tokens
        print("\nMinting Teko tokens...")
        results = await teko.mint_all(private_key)
        for token, result in results:
            print(f"{token} mint result: {result}")
        
        # Example swap on Bebop
        print("\nPerforming Bebop swaps...")
        swap_pairs = [
            (config['contracts']['teko']['tkETH'], config['contracts']['teko']['tkUSDC'], 1000000000000000000),
            (config['contracts']['teko']['tkUSDC'], config['contracts']['teko']['tkWBTC'], 1000000)
        ]
        results = await bebop.perform_swaps(private_key, swap_pairs)
        for pair, result in results:
            print(f"Bebop swap {pair} result: {result}")
        
        # Example swap on GTE
        print("\nPerforming GTE swaps...")
        swap_pairs = [
            (config['contracts']['teko']['tkETH'], config['contracts']['teko']['tkUSDC'], 1000000000000000000, 0),
            (config['contracts']['teko']['tkUSDC'], config['contracts']['teko']['tkWBTC'], 1000000, 0)
        ]
        results = await gte.perform_swaps(private_key, swap_pairs)
        for pair, result in results:
            print(f"GTE swap {pair} result: {result}")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())