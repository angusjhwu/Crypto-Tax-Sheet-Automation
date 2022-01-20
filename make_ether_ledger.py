import requests
from datetime import datetime as dt
import etherscan_methods as esm

address = ""
token = ""

# Test balance
url = esm.get_balance_url(address, token)

response = requests.get(url)

content = response.json()
eth = esm.wei_to_eth(content.get("result"))
print('Current ETH Balance: ' + str(eth))


# Test tx
url = esm.get_tx_url(address, token)

response = requests.get(url)
content = response.json()
result = content.get('result')

for n, tx in enumerate(result):
    status = tx.get('isError')

    print()
    if int(status):
        print(str(n+1), '**FAILED** ===========')
    else:
        print(str(n + 1), '===========')
    esm.print_tx(address, tx)
