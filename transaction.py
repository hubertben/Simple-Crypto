from hashlib import sha256

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