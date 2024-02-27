def solve(arr):
    n = len(arr)
    count_of_elements_decreasing = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            count_of_elements_decreasing += 1
    
    return count_of_elements_decreasing <= 1

arr = [10, 10, 5, 7, 10]
print(solve(arr))