def solve(cities):
    curr_max = float('-inf')
    ans = 0
    n = len(cities)
    for i in range(n - 1, -1, -1):
        if cities[i] > curr_max:
            ans += 1
            curr_max = cities[i]
    
    return ans

print(solve([3, 7, 8, 3, 6, 1]))
        