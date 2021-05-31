from hashlib import sha256
import random

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