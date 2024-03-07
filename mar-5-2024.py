def perform_op(op_sign, prev, curr):
    if prev == None:
        return curr
    if op_sign == '|':
        return prev | (True if curr == 'T' else False)
    elif op_sign == '&':
        return prev & (True if curr == 'T' else False)
    return prev ^ (True if curr == 'T' else False)

def solve(arr):
    
    prev = None
    curr = None
    n = len(arr)
    prefix = [True for _ in range(n)]
    suffix = [True for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            if i == 0:
                prefix[i] = True if arr[i] == 'T' else False
            else:
                perform_op(arr[i - 1], prefix[i - 1], prefix[i])
        else:
            prefix[i] = prefix[i - 1]
    
    for i in range(n - 1, -2, -1):
        if i % 2 == 0:
            if i == n - 1:
                suffix[i] = True if arr[i] == 'T' else False
            else:
                perform_op(arr[i - 1], suffix[i - 1], suffix[i])
        else:
            suffix[i] = suffix[i - 1]
    
    ans = 1
    for i in range(0, n, 2):
        prev = prefix[i - 1] if i > 0 else None
        curr = True if arr[i] == 'T' else False
        for j in range(i + 2, n, 2):
            curr = perform_op(arr[j - 1], curr, arr[j])
            end = suffix[j + 1] if j < n - 1 else None
            if j < n - 1:
                curr = perform_op(arr[j + 1], curr, end)  
            if curr:
                ans += 1

    return ans
print(solve(['F', '|', 'T', '&', 'T']))

