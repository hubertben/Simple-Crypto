from hashlib import sha256
from chain import Chain
from user import User
from block import Block
from transaction import Transaction

def hex_to_bin(hex):
    hexa = str(hex)
    return bin(int(hexa, 16))[2:]

def read_from_file():
    with open("ledger.txt", "r") as txt_file:
        return txt_file.read().splitlines()

def process_input_information(file_information):
    user_list = []
    transaction_list = []

    for y in file_information:
        if(y == '-=-'):
            break

        if(y[0] == '%'):
            y = y[1:]
            temp = y.split(' ')
            q = temp[2]
            q = q[1:]
            user_list.append(User(temp[0], '000', float(q)))
        
        if(y[0] == '&'):
            y = y[1:]
            
            temp = y.split(' ')
            q = temp[3]
            q = q[1:]

            sender = None
            recipient = None

            for u in user_list:
                if(temp[0] == u.name):
                    sender = u
                if(temp[2] == u.name):
                    recipient = u

            transaction_list.append(Transaction(sender, recipient, float(q)))

    return [user_list, transaction_list]



file_information = read_from_file()
data = process_input_information(file_information)

working_chain = Chain()
current_block = Block(data[0], 0)
current_block.transaction_list = data[1]
current_block.get_transactions()