from random import randint

def selection_sort(lst):
    """
    Input: List of integers not in any fixed order
    Output: List of integers in ascending order
    """
    length = len(lst)
    for idx in range(length):
        min_element = lst[idx]
        min_idx = idx
        for jdx in range(idx+1, length):
            if lst[jdx] < min_element:
                min_element = lst[jdx]
                min_idx = jdx
        lst[idx], lst[min_idx] = lst[min_idx], lst[idx]
    return lst

for test in range(10):
    length_of_lst = randint(1, 21)
    lst = [randint(-10, 10) for i in range(length_of_lst)]
    print("List before sorting: " + str(lst))
    sorted_lst = selection_sort(lst)
    print("List after sorting: " + str(sorted_lst))
    print("-------------------------------")

    