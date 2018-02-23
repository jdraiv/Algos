import random


def random_list():
    l_data = []

    for n in range(random.randint(2, 5)):
        l_data.append(random.randint(0, 200))

    return l_data


class Tests(object):
    def __init__(self, algo):
        self.correct = 0
        self.incorrect = 0
        self.algo = algo

    def show_results(self):
        print("%s: Passed" % self.correct)
        print("%s: Failed" % self.incorrect)

    def sort_custom_input(self, i):
        if sorted(self.algo(i)):
            self.correct += 1
        else:
            self.incorrect += 1

    def sort_random_inputs(self):
        for c in range(random.randint(10, 20)):
            if sorted(self.algo(random_list())):
                self.correct += 1
            else:
                self.incorrect -= 1

