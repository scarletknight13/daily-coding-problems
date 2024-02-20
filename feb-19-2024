def solve(pattern, s):
    n, m = len(pattern), len(s)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] == n:
                    return j - n
    
    return -1


def alt_sol(pattern, s):
    possible_beginnings = []
    n = len(s)
    m = len(pattern)
    for id, val in enumerate(s):
        if val == pattern[0]:
            possible_beginnings.append(id)
    
    for i in possible_beginnings:
        s_pointer = i
        pattern_pointer = 0
        mathched_length = 0
        while(s_pointer < n and pattern_pointer < m and s[s_pointer] == pattern[pattern_pointer]):
            mathched_length += 1
            s_pointer += 1
            pattern_pointer += 1
        
        if mathched_length == m:
            return i
    
    return -1
    

print(alt_sol('ab', 'xacdabx'))
print(alt_sol('ab', 'abcabc'))
print(alt_sol('abd', 'abcabd'))
print(alt_sol('ab', 'adffgaf'))
