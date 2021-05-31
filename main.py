
# Created by Ben Hubert

from chain import Chain
from block import Block
from functions import read_from_file, process_input_information

file_information = read_from_file()
data = process_input_information(file_information)

working_chain = Chain()
current_block = Block(data[0], 0)
current_block.transaction_list = data[1]
current_block.get_transactions()