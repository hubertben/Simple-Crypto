from transaction import Transaction
from user import User

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