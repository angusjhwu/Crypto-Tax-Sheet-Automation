import config
import requests
import etherscan_methods as esm


# Test tx
url = esm.get_tx_url(config.ADDRESS, config.ES_TOKEN)
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
    esm.print_tx(config.ADDRESS, tx)
