import sys
import numpy as np
from Bio import AlignIO

def handle_input_file(FILE_PATH, FORMAT):
    try:
        seq_list = AlignIO.read(FILE_PATH, FORMAT)
    except Exception as e:
        error_string = f'Format error in {FILE_PATH}: '
        sys.exit(error_string + str(e))
        

    seq_list = [sequence.seq._data for sequence in seq_list]

    NUMBER_OF_SEQUENCES = len(seq_list)
    SEQUENCE_LENGTH = len(seq_list[0])
    new_array = np.empty([NUMBER_OF_SEQUENCES, SEQUENCE_LENGTH], dtype='U')

    for INDEX, SEQUENCE in enumerate(seq_list):
        new_array[INDEX] = np.array(list(SEQUENCE))

    return new_array
