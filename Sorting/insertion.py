

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Tester import Tests


def insertion_sort(l):
    for c in range(1, len(l)):
        current_num = l[c]
        new_pos = c
        cont = True

        while cont and new_pos >= 1:
            if current_num <= l[new_pos - 1]:
                new_pos -= 1
            else:
                cont = False

        l.insert(new_pos, current_num)
        l.pop(c + 1)

    return l


Tests().random_test_sort(insertion_sort)