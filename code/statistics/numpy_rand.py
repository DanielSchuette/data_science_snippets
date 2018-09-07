#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import numpy as np

# initialize a random seed
np.random.seed(42)

# generate a random sample from a given 1-D array `a'
# optional arguments let you specify:
#   1. what the output shape is going to be (`size')
#   2. whether to sample with replacement (`replace')
#   3. whether the entries in `a' have different probabilities
#      to be drawn during sampling (`p')
sample = np.array([1, 2, 3, 4, 5, 6])
print(np.random.choice(sample))
