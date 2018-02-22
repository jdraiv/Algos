import unittest


def random_list():
    import random

    l_data = []

    for n in range(random.randint(2, 5)):
        l_data.append(random.randint(0, 200))

    return l_data


class Tests(object):
    def show_results(self, correct, incorrect):
        print("%s: Passed" % correct)
        print("%s: Failed" % incorrect)

    """
        Parameters: (spec_input, inputs, algo)
        spec_input: Single list for testing.
        inputs: List with more inputs for testing.
        algo: Algorithm that is being implemented.

    """
    def test_sort(self, spec_input, inputs, algo):
        pass

    """
        Test the algorithm implemented using random generated data.
    """
    def random_test_sort(self, algo):
        random_l = random_list()
        correct, incorrect = 0, 0

        if sorted(algo(random_l)):
            correct += 1
        else:
            incorrect += 1

        self.show_results(correct, incorrect)

