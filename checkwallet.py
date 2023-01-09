import requests

# Open the file with the list of Ethereum wallet addresses
with open('wallet_list.txt', 'r') as f:
    # Read the wallet addresses from the file
    wallet_list = f.readlines()

# Strip the newline characters from the wallet addresses
wallet_list = [wallet.strip() for wallet in wallet_list]

# Ethereum API endpoint for getting the balance of a wallet
eth_api_endpoint = "https://phoenixplorer.com/api?module=account&action=eth_get_balance&address="

# Iterate through the list of wallets
with open('wallet_results.txt', 'w') as f:
    for wallet in wallet_list:

        response = requests.get(eth_api_endpoint + wallet)
    # Check the response status code to make sure it was successful
        if response.status_code == 200:
         data = response.json()
        # Get the balance of the wallet in ETH
         balance = data['result']
         balanceconv = int(balance, 16) / 10**18
        # Check if the balance is greater than 5000 ETH
        if balanceconv >= 5000:
            print("wallet: " + wallet + "  || Balance: " + str(balanceconv) + "\n")
        else:
            f.write("Oops, user " + wallet + " has a balance of " + str(balanceconv) + "  +\n")
    else:
        f.write("Error getting balance for wallet " + wallet)
