import numpy as np

### Private functions
def _create_count_matrix(SEQUENCE_PAIRS):
    return_matrix = np.zeros(shape=(20,20))
    
    ALPHABET = ('A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V')
    alphabet_dictionary = {}
    for i, letter in enumerate(ALPHABET):
        alphabet_dictionary[letter] = i
    
    for i,_ in enumerate(SEQUENCE_PAIRS[0]):
        a = SEQUENCE_PAIRS[0][i]
        b = SEQUENCE_PAIRS[1][i]
        
        if a == '-' or b == '-':
            continue
        
        return_matrix[alphabet_dictionary[b]][alphabet_dictionary[a]] = return_matrix[alphabet_dictionary[b]][alphabet_dictionary[a]] + 1
        
    return return_matrix

### Interface
def create_count_matrices(SEQUENCE_PAIRS):
    COUNT_MATRIX_LIST = [_create_count_matrix(SEQUENCE_PAIR) for SEQUENCE_PAIR in SEQUENCE_PAIRS]

    return COUNT_MATRIX_LIST