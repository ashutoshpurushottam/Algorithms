def quick_sort(arr):
    if len(arr) < 2:
        return arr 
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(great)

arr = [3, 5, 1, 4, 2]
sorted_arr = quick_sort(arr)
print(sorted_arr)