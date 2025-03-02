def binary_search(*, arr: list, item: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# examples:
list = [1, 2, 8, 10, 15]
print(binary_search(arr=list, item=10))  
print(binary_search(arr=list, item=5))