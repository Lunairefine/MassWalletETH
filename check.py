from web3 import Web3

web3 = Web3(Web3.HTTPProvider('YOUR_INFURA_PROJECT_ID')) #// ADD YOUR API IN ('')

def read_wallet_addresses(filename):
    with open(filename, 'r') as file:
        wallet_addresses = file.readlines()
    wallet_addresses = [address.strip() for address in wallet_addresses if address.strip()]
    return wallet_addresses

def check_eth_balance(wallet_address):
    balance = web3.eth.get_balance(wallet_address)
    balance_eth = web3.from_wei(balance, 'ether')
    return balance_eth

if __name__ == '__main__':
    filename = 'eth_address.txt'  # Nama file yang berisi alamat dompet Ethereum
    wallet_addresses = read_wallet_addresses(filename)
    
    for address in wallet_addresses:
        balance_eth = check_eth_balance(address)
        print(f'The ETH balance of the address {address} is {balance_eth} ETH')
