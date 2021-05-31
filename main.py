from hashlib import sha256
import random

def hex_to_bin(hex):
    hexa = str(hex)
    return bin(int(hexa, 16))[2:]

class User:

    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

        self.block = None

        self.ID = 0

        self.generate_id()

    def add_working_block(self, block):
        self.block = block

    def generate_id(self):
        id = self.name + '' + self.password
        self.ID = sha256(id.encode()).hexdigest()

    def get_user_data(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('User ID:', self.ID)
        print('User Name:', self.name)
        print('User Password:', self.password)
        print('User Balance:', self.balance)

class Transaction:

    def __init__(self, sender, recipient, ammount):
        self.sender = sender
        self.recipient = recipient
        self.ammount = ammount

        self.ID = 0

        self.generate_id()
        verification = self.transfer()

        if(verification == False):
            print('Transaction', self.ID, 'unable to be completed')
    
    def generate_id(self):
        id = self.sender.name + '' + self.recipient.name + '' + str(self.ammount)
        self.ID = sha256(id.encode()).hexdigest()

    def transfer(self):

        if(self.ammount > self.sender.balance):
            return False
        else:
            self.sender.balance = round(self.sender.balance - self.ammount, 2)
            self.recipient.balance = round(self.recipient.balance + self.ammount, 2)
            return True

    def get_transaction(self):
        return (self.ID, self.sender, self.recipient, self.ammount)

class Block:

    def __init__(self, user_list, chain_POV):

        for u in user_list:
            u.add_working_block(self)

        self.transaction_list = []
        self.user_list = user_list

        self.block_pow_len = int(random.randint(3, 5))

        self.previous_block_POW = chain_POV
        self.proof_of_work = 0

    def verify_proof_of_work(self, key):
        verify = True
        for i in range(self.block_pow_len):
            print(key[i])
            if(key[i] != '0'):
                verify = False
        
        if(verify):
            self.proof_of_work = key
            print('Approved')

    def get_transactions(self):
        print('Block Proof of Work', self.proof_of_work)
        print('Block Previous Block POW', self.previous_block_POW)
        print('\nUser List')
        for u in self.user_list:
            u.get_user_data()

        print('\nTransaction List')
        for t in self.transaction_list:
            print('    - Transaction ID', t.ID)
            print('    - Sender', t.sender.name)
            print('    - Recipient', t.recipient.name)
            print('    - Ammount', t.ammount)
            print('')


class Chain:

    def __init__(self):
        self.block_list = []
    
    def push(self, block):
        self.block_list.append(block)


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