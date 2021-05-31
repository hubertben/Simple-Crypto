class Chain:

    def __init__(self):
        self.block_list = []
    
    def push(self, block):
        self.block_list.append(block)