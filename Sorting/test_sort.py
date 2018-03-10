
import random
import time


class Tests(object):
    def __init__(self, algo):
        self.correct = 0
        self.incorrect = 0
        self.algo = algo

    def run_time(self):
        start_time = time.process_time()
        return start_time

    def show_results(self):
        print("%s: Passed" % self.correct)
        print("%s: Failed" % self.incorrect)

    def sort_custom_input(self, i):
        t = self.run_time()

        if sorted(self.algo(i)):
            self.correct += 1
            print("Test passed in %s seconds" % (time.process_time() - t))
        else:
            self.incorrect += 1
            print("Test failed in %s seconds" % (time.process_time() - t))

    def sort_random_inputs(self):
        for c in range(random.randint(1, 50)):
            c = range(0, 11000)
            random_l = random.sample(c, random.randint(1, 200))

            t = self.run_time()

            if sorted(self.algo(random_l)):
                self.correct += 1
                print("Test passed in: %s seconds" % (time.process_time() - t))
            else:
                self.incorrect -= 1
                print("Test failed in: %s seconds" % (time.process_time() - t))
