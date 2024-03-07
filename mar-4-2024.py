# Good morning! Here's your coding interview problem for today.
# This problem was asked by Microsoft.
# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 
# For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

def solve(s, pattern):
    window_size = len(pattern)
    ans = []
    curr_s = ''
    for i, val in enumerate(s):
        curr_s += val
        if i >= window_size - 1:
            if i >= window_size:
                curr_s = curr_s[1:]
            # print(curr_s)
            if curr_s == pattern:
                ans.append(i - window_size + 1)
    
    return ans

print(solve('abracadabra', 'abr'))