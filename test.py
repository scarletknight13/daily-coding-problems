def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    
    # Step 1: Find the minimum and maximum elements in the array
    min_num = min(nums)
    max_num = max(nums)
    
    # Step 2: Compute the bucket size and number of buckets
    bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
    num_buckets = (max_num - min_num) // bucket_size + 1
    
    # Step 3: Initialize buckets
    buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]
    
    # Step 4: Place elements into buckets
    for num in nums:
        index = (num - min_num) // bucket_size
        buckets[index][0] = min(buckets[index][0], num)
        buckets[index][1] = max(buckets[index][1], num)
    
    # Step 5: Compute maximum gap
    max_gap = 0
    prev_max = min_num
    for bucket in buckets:
        if bucket[0] == float('inf'):
            continue
        max_gap = max(max_gap, bucket[0] - prev_max)
        prev_max = bucket[1]
    
    return max_gap

print( maximum_gap([1, 2838, 6001, 8000, 10000]) )