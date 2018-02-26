
import random


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
        for c in range(random.randint(1, 200)):
            c = range(0, 11000)
            random_l = random.sample(c, random.randint(1, 200))

            if sorted(self.algo(random_l)):
                self.correct += 1
            else:
                self.incorrect -= 1