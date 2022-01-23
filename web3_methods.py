import config
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))


def print_tx(address, tx):
    hx = tx.get('hash')
    tx_from = tx.get('from')
    tx_to = tx.get('to')
    value = tx.get('value')
    gas = tx.get('gas')
    gas_price = tx.get('gasPrice')

    print('Tx Hash:', hx.hex())
    print('Value:', w3.fromWei(int(value), 'ether'), 'ETH')
    if tx_from == address.lower():
        print('Sent, from user to', tx_to)
    elif tx_to == address.lower():
        print('Received, from', tx_from, 'to user')
    else:
        print('Sent, from', tx_from, 'to', tx_to)
    print('Gas: ', w3.fromWei(int(gas), 'ether'))
    print('Gas Fee:', w3.fromWei(int(gas_price), 'ether'))

def main():
    print(w3.eth.block_number)

    bal = w3.eth.get_balance(config.ADDRESS)
    eth_bal = w3.fromWei(bal, 'ether')
    print(eth_bal, 'ETH')

    tx = w3.eth.get_transaction("0xa5c1a20e649507fc7fe25663d043b6646cafc9a65d96480865f435c528bd613f")
    print_tx(config.ADDRESS, tx)


if __name__ == '__main__':
    main()



