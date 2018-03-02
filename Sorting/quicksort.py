
import random


# Select a random pivot
# Elements on the left of the pivot should be lower and the elements on
# the right side of the pivot should be greater

# Counter Variables
# ! I = Index of smaller element. !
# ! J = Loop variable             !

def quick_sort(l):
    def partition(l):
        pivot_index = len(l) - 1
        pivot_value = l[pivot_index]
        i = -1
        j = 0

        for c in range(len(l) - 1):
            current_elem = l[c]
            if current_elem < pivot_value:
                # Increment I variable
                i += 1

                # Swap the list
                l[c] = l[i]
                l[i] = current_elem

        # Update pivot pos
        l.pop(pivot_index)

        # Update pivot index
        pivot_index = i + 1
        l.insert(pivot_index, pivot_value)

        return l
    partition(l)


l_one = [7, 2, 1, 8, 6, 3, 5, 4]
quick_sort(l_one)

