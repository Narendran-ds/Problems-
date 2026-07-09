def largest_number(arr):
    if len(arr)==0:
        return None
    largest = float("-inf")
    smallest = float("inf")
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num;
    return largest, smallest
arr=[12,33,43,1,33]
print(largest_number(arr))