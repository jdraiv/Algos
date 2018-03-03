
from test_sort import Tests
import random


def bogosort(l):
    for c, element in enumerate(l):
        random_pos = random.randint(0, len(l))
        l.pop(c)
        l.insert(random_pos, element)
    return l


def is_sorted(l):
    if sorted(l) == l:
        return True
    else:
        return False


def apply_bogosort(l):
    list = bogosort(l)

    while not is_sorted(list):
        list = bogosort(l)
    return list


test = Tests(apply_bogosort)
test.sort_random_inputs()
