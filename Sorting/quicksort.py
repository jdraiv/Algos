
from test_sort import Tests

# Elements on the left of the pivot should be lower and the elements on
# the right side of the pivot should be greater


def quicksort(l):
    left = []
    right = []
    equal = []

    if len(l) > 1:
        pivot = l[0]

        for elem in l:
            if elem < pivot:
                left.append(elem)
            elif elem > pivot:
                right.append(elem)
            else:
                equal.append(elem)

        return quicksort(left) + equal + quicksort(right)
    return l


test = Tests(quicksort)
test.sort_random_inputs()
test.show_results()

