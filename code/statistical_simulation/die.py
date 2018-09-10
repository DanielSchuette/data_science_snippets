import sys

import numpy as np


class Die():
    """
    class Die has methods and attributes that are needed
    to statistically simulate the throwing of a die
    specifically, a die has
        `sides' - number of sides (default is 6)
        `probabilities  - list giving the probability of
                          outcomes when throwing the die
        `.throw(x)'     - returns a list of outcomes
                          after throwing the die `n' times
        `.plot()'       - TODO: implement!
    """

    def __init__(self, sides=6, probabilities=None):
        # define custom error values for this class
        self.noneError = "must be `None'"
        self.probError = "must be of type list"
        self.floatError = "must be of type float"

        # create a list with `sides' number of die sides
        if isinstance(sides, int):
            self.sides = list(range(sides))
        else:
            print("`sides' must be of type integer")
            sys.exit(1)

        # if the user indicated a list of probabilities,
        # assign it to `self.probabilities'
        # it is tested if `probabilities' is a list with float elements
        if probabilities:
            if isinstance(probabilities, list):
                for prob in probabilities:
                    if not isinstance(prob, float):
                        if (prob < 0.0) and (prob > 1.0):
                            print("argument `probabilities' " +
                                  self.floatError + ", <= 1.0 and >= 0.0")
                            sys.exit(1)
                self.probabilities = probabilities
            else:
                print("argument `probabilities' " + self.noneError + " or " +
                      self.listError + " with len=`sides'")
                sys.exit(1)
        # otherwise, assign a list of equal probabilities
        else:
            equal_chance = 1.0 / len(self.sides)
            self.probabilities = [equal_chance for i in self.sides]

        # finally, check if `probabilities' and `sides' have the same length
        if len(self.probabilities) is not len(self.sides):
            print("`probabilities' and `sides' must have the same length")
            sys.exit(1)

    def throw(self, times=1, verbose=False):
        # if verbose output is wanted, print specifics of the throw
        if verbose:
            print("throwing {} times".format(times))
            print("die has {} sides".format(self.sides))
            print("probabilities associated with these sides: {}".format(
                self.probabilities, ))

        # simulate `times' outcomes using `np.random.choice'
        outcome = np.random.choice(
            self.sides,
            size=times,
            p=self.probabilities,
        )
        return outcome

    def plot():
        pass
