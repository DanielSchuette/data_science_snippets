#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

import die


def main():
    """
    examples of how to use python for statistical simulation

    simulation is a way to model random events by repeatedly
    sampling from a probability distribution that is likely
    to underlie the actual real-life event

    usually, the workflow is as follows:
        1. define possible outcomes
        2. assign probabilities to outcomes
        3. define the relationship between outcomes/variables
        4. sample repeatedly from the appropriate probability
           distribution to simulate possible outcomes
        5. visualize/analyze outcomes
    """
    # fair die simulation
    side_number = int(input("how many sides does your die have? "))
    d = die.Die(sides=side_number, probabilities=None)
    print("outcome: {}".format(d.throw(times=5, verbose=True)))


if __name__ == "__main__":
    main()
    sys.exit(0)
