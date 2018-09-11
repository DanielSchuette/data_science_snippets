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
    # two dies are thrown 1000 times each and if the results
    # are the same, the player wins
    num_throws = 1000
    d1 = die.Die(sides=6, probabilities=None)
    d2 = die.Die(sides=6, probabilities=None)
    outcomes = []
    for i in range(num_throws):
        out = (d1.throw(1)[0], d2.throw(1)[0])
        outcomes.append(out)

    # then, count the number of wins
    win_counter = 0
    for val in outcomes:
        if val[0] == val[1]:
            win_counter += 1

    # finally, print out the proportion of wins
    print(("out of {} throws you won {}%").format(num_throws,
                                                  win_counter / num_throws))


if __name__ == "__main__":
    main()
    sys.exit(0)
