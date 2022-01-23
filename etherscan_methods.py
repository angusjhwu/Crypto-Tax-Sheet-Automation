import config
from datetime import datetime as dt
import requests


def get_balance_url(address, token):
    return ('https://api.etherscan.io/api'
            '?module=account'
            '&action=balance'
            '&address=' + address +
            '&tag=latest'
            '&apikey=' + token)


def get_tx_url(address, token, action='', num_tx=30, start_block=0, end_block=99999999):
    if action == 'internal':
        action = 'txlistinternal'
    else:
        action = 'txlist'

    return ('https://api.etherscan.io/api'
            '?module=account'
            '&action=' + action +
            '&address=' + address +
            '&startblock=' + str(start_block) +
            '&endblock=' + str(end_block) +
            '&page=1'
            '&offset=' + str(num_tx) +
            '&sort=asc'
            '&apikey=' + token)


def wei_to_eth(wei):
    return int(wei) * 10 ** -18


def print_tx(address, tx):
    time = tx.get('timeStamp')
    hx = tx.get('hash')
    status = tx.get('isError')
    tx_from = tx.get('from')
    tx_to = tx.get('to')
    value = tx.get('value')
    gas = tx.get('gas')
    gas_price = tx.get('gasPrice')
    gas_used = tx.get('gasUsed')
    cx = tx.get('confirmations')

    print('Time:', dt.fromtimestamp(int(time)), 'UTC')
    print('Tx Hash:', hx)
    print('Confirmations:', cx)
    print('Value:', wei_to_eth(int(value)), 'ETH')
    if tx_from == address.lower():
        print('Sent, from user to', tx_to)
    elif tx_to == address.lower():
        print('Received, from', tx_from, 'to user')
    else:
        print('Sent, from', tx_from, 'to', tx_to)
    print('Gas Fee:', wei_to_eth(int(gas_used) * int(gas_price)), 'ETH')


def main():
    # Test balance
    url = get_balance_url(config.ADDRESS, config.ES_TOKEN)
    response = requests.get(url)
    content = response.json()
    eth = wei_to_eth(content.get("result"))
    print('Current ETH Balance: ' + str(eth))


    # Test tx
    url = get_tx_url(config.ADDRESS, config.ES_TOKEN, '', 1)
    response = requests.get(url)
    content = response.json()
    tx = content.get('result')[0]
    status = tx.get('isError')

    if status:
        print("Transaction successful")
    else:
        print("Transaction failed")
    print_tx(config.ADDRESS, tx)


if __name__ == '__main__':
    main()
