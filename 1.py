from bitcoin.rpc import RawProxy

def Calculate():
    p = RawProxy()
    transactions = p.decoderawtransaction(p.getrawtransaction(raw_input("Enter ID:")));
    starting = 0
    ending = 0
    for single in transactions.get('vin'):
        allt = p.decoderawtransaction(p.getrawtransaction(single.get('txid'))).get('vout')
        for transaction in allt:
            n = transaction.get('n')
            if n == single.get('vout'):
                starting += transaction.get('value')
    for transaction in transactions.get('vout'):
        ending += transaction.get('value')
    fee = starting - ending
    print("Fee Paid: ", fee, " btc")

Calculate()
