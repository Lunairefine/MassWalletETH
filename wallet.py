from eth_account import Account
import os

def generate_eth_wallet():
    private_key = os.urandom(32).hex()
    account = Account.from_key(private_key)
    public_key = account._key_obj.public_key
    address = account.address
    return {
        'private_key': private_key,
        'public_key': public_key,
        'address': address
    }

num_wallets = 1000 #///////////  HOW MANY WALLETS YOU WANT TO CREATE
addresses = []
private_keys_and_addresses = []

for i in range(num_wallets):
    wallet = generate_eth_wallet()
    addresses.append(wallet['address'])
    private_keys_and_addresses.append(f"{wallet['private_key']} {wallet['address']}")
    print(f"Wallet {i+1} - Address: {wallet['address']}")

with open('eth_address.txt', 'w') as file:
    for address in addresses:
        file.write(address + '\n')

with open('privatekeys_and_address.txt', 'w') as file:
    for item in private_keys_and_addresses:
        file.write(item + '\n')

print("All addresses have been saved to eth_address.txt")
print("All private keys and addresses have been saved to privatekeys_and_address.txt")
