from hashlib import sha256

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

