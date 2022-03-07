blockchain = [] # [[]] or [] ([])


def get_last_blockchain_value():
    return blockchain[-1]  # blockchain[-1

# add_value(transaction_amount, last_transaction=[1]):
def add_value(transaction_amount, last_transaction=[1]):   # add_value(transaction_amount, last_transaction):  # last_transaction
    # get_last_blockchain_value(),
    blockchain.append([last_transaction, transaction_amount]) # ([blockchain[-1], 3.4]) :1 :  last_transaction, transaction_amount
    # print(blockchain)  # blockchain[0]
tx_amount = float(input("Your transaction amount please: "))
add_value(tx_amount) # (2,[1]) add_value(txt_transaction)

tx_amount = float(input("Your transaction amount please: "))
add_value(tx_amount, get_last_blockchain_value()) # 0.9, (last_transaction=get_last_blockchain_value(), transaction_amount=0.9)

tx_amount = float(input("Your transaction amount please: "))
add_value(tx_amount, get_last_blockchain_value()) # get_last_blockchain_value(), 10.89

print(blockchain)  # blockchain[0]
