# Good morning! Here's your coding interview problem for today.
# This problem was asked by Facebook.
# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

def solve(arr):
    n = len(arr)
    count_of_elements_decreasing = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            count_of_elements_decreasing += 1
    
    return count_of_elements_decreasing <= 1

arr = [10, 10, 5, 7, 10]
print(solve(arr))