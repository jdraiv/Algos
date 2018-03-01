
from test_sort import Tests


def bubble_sort(l):
    tail = len(l) - 1

    while tail >= 0:
        for c in range(tail):
            if l[c + 1] < l[c]:
                old_val = l[c]

                l[c] = l[c + 1]
                l[c + 1] = old_val
        tail -= 1
    return l


test = Tests(bubble_sort)
test.sort_random_inputs()
test.show_results()
