#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

# the numpy.random module provides a suit of functions to draw random
# samples from probability distributions, e.g. the Poisson distribution
# parameters: lambda (`lamb'), sample size (`size')
lamb, size = 5, 1000
poisson_dist = np.random.poisson(lamb, size)

# seaborn's `distplot' can be used to visualize probability distributions
sns.distplot(poisson_dist)
# plt.show("hold")

# to randomly shuffle values in a list or numpy array, `np.random.shuffle'
# can be used
sorted_list = list(range(10))
print("sorted: {}".format(sorted_list))
shuffled_list = sorted_list.copy()  # `np.random.shuffle' will shuffle in-place
np.random.shuffle(shuffled_list)
print("shuffled: {}".format(shuffled_list))
