def second_largest(arr):
    if len(arr) < 2:
        return None
    first = float("-inf")
    second = float("-inf")
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num 
        
    return None if second == float("-inf") else second

arr=[12,33,43,1,33]
print(second_largest(arr))