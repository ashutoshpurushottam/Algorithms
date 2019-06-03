def binary_search(lst, val):
    """
    lst: input list where number should be searched
    val: the value to be searched in the input list 

    assumption: lst is sorted in ascending order

    Returns index of the number if it is found in the list
    else it returns -1 indicating the value is not present 
    in the list.
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if lst[mid] == val:
            return mid 
        elif lst[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1 
    

lst = [2, 13, 19, 28, 31, 39, 43, 51, 59, 68, 89, 90, 98, 99]

print(binary_search(lst, -1))
print(binary_search(lst, 23))
print(binary_search(lst, 31))
print(binary_search(lst, 2))
print(binary_search(lst, 99))
print(binary_search(lst, 100))

# Suppose you have a sorted list of 128 names, and you’re searching 
# through it using binary search. What’s the maximum number of steps 
# it would take?
# Ans: 7 

# Suppose you double the size of the list. What’s the maximum number 
# of steps now?
# Ans: 8