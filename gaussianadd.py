# adds gaussian noise to input segment
# simulates Yi's program
import numpy as np


def add_gauss(chunk, chunk_size):
    noise = np.random.normal(0, .0001, chunk_size*4)
    # check for 2 second data
    # if #someCheck:
    #     # print('Received 2s data')
    return np.add(chunk, noise)
    return chunk
