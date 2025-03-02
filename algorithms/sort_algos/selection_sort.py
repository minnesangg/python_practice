def find_smallest(*, arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(*, arr: list) -> list:
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr=arr)
        new_array.append(arr.pop(smallest))
    return new_array

#example:
print(selection_sort(arr=[2, 3, 1, 8, 5]))
