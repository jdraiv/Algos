
from SortTest import Tests


def selection_sort(l):
    for c, pos in enumerate(l):
        c_lowest = pos

        for element in range(c, len(l)):
            if l[element] < c_lowest:
                c_lowest = l[element]

        l.pop(l.index(c_lowest))
        l.insert(c, c_lowest)
    return l


test = Tests(selection_sort)
test.sort_random_inputs()
test.show_results()
