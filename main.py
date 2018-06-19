import os
import sys
import numpy as np
from scipy.linalg import eig
from handle_input_file import handle_input_file
from match_closest_pair import match_closest_pairs
from create_count_matrices import create_count_matrices
from comp_posterior_JC import comp_posterior_JC
from matrix_weight import matrix_weight
from estimate_q import estimate_q
from simple_estimation import simple_estimation

# ### Preamble
# os.system('cls')

### Private
def _main():
    #   Create count matrix list
    FILE_NAME = "tests\\test_files\\main_test\\testcase1_20seqs.fa"
    FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILE_NAME)

    SEQUENCE_LIST = handle_input_file(FILE_PATH)
    CLOSEST_PAIRS = match_closest_pairs(SEQUENCE_LIST)
    COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)

    #   These are constant throughout the iterations
    sumMatrix = sum(0.5 * (matrix + matrix.transpose()) for matrix in COUNT_MATRIX_LIST)
    P_SUM = sumMatrix / sumMatrix.sum(axis=1, keepdims=True)    # Make every row sum to 1

    eigenValues, VR = eig(P_SUM, left=False, right=True)
    eigenValues = eigenValues.real
    VL = np.linalg.inv(VR)

    # #
    # # Find the index of the eigenvector corresponding to Q's zero eigenvalue.
    # # This is recognized as the row (because we will be looking at the 'right'
    # # eigenvectors, not the usual left) with all positive or all negative elements.
    # #
    zeroEigenVectorsList = [eigenVector for eigenVector in VL if all(eigenVector > 0) or all(eigenVector < 0)]
    assert len(zeroEigenVectorsList) == 1, "To many or to few potential zero eigenvectors"
    EQ = zeroEigenVectorsList.pop()
    EQ = EQ / EQ.sum()  # Make elements of EQ sum to 1

    #   Get a first simple estimate of Q using a Jukes-Cantor model
    DIST_SAMPLES = np.arange(1, 400, 5)
    POSTERIOR = comp_posterior_JC(COUNT_MATRIX_LIST, DIST_SAMPLES)   # posterior.shape = (10, 80). Rows are identical to Octave but in different order
    W = POSTERIOR.sum(axis=0)
    PW = matrix_weight(COUNT_MATRIX_LIST, POSTERIOR, DIST_SAMPLES)   #   Seems identical to octave. Alot of NaN
    Q = estimate_q(PW, W, VL, VR, EQ, DIST_SAMPLES)

    #   Set loop variables
    difference = float("inf")
    iteration = 0
    THRESHOLD = 0.001
    MAX_ITERATIONS = 10

    #   Calculate Q
    while (iteration < MAX_ITERATIONS and difference > THRESHOLD):
        iteration += 1
        Q, difference = simple_estimation(COUNT_MATRIX_LIST, Q, VL, VR, EQ, DIST_SAMPLES)

    return Q, EQ

### Interface
def main():
    Q, EQ = _main()
    return Q, EQ
