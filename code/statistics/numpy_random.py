#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

import numpy as np

# initialize a random seed
try:
    seed = int(input("please input an integer to use as a random seed: "))
except ValueError or TypeError:
    sys.exit(1)

np.random.seed(seed)

# generate a random sample from a given 1-D array `a'
# optional arguments let you specify:
#   1. what the output shape is going to be (`size')
#   2. whether to sample with replacement (`replace')
#   3. whether the entries in `a' have different probabilities
#      to be drawn during sampling (`p')
sample = np.array([1, 2, 3, 4, 5, 6])
rand_sampled = np.random.choice(sample)
print(rand_sampled)
