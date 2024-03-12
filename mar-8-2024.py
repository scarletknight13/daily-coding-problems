from random import *

def reverse_list(arr):
    return arr[::-1]

def solve(arr):
    unsorted_pointer = 0
    n = len(arr)
    while unsorted_pointer < n:
        # print('here')
        curr_min = float('inf')
        curr_min_id = unsorted_pointer
        for i in range(unsorted_pointer, n):
            if arr[i] < curr_min:
                curr_min = arr[i]
                curr_min_id = i
        arr[unsorted_pointer:curr_min_id+1] = reverse_list(arr[unsorted_pointer:curr_min_id+1])
        unsorted_pointer += 1
    

            
arr_size = randint(4, 10)
arr = []
for i in range(arr_size):
    arr.append(randint(1, 50))
print('arr before sort ', arr)
solve(arr)
print('arr after sort ', arr)