
# Good morning! Here's your coding interview problem for today.
# This question was asked by Zillow.
# You are given a 2-d matrix where each cell represents number of coins in that cell. 
# Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.
# For example, in this matrix

###########
# 0 3 1 1 #
# 2 0 0 4 #
# 1 5 3 1 #
###########
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins

def solve(prob_mat):
    n, m = len(prob_mat), len(prob_mat[0])
    dp = [[0 for x in range(m) ] for y in range(n) ]
    for i in range(n):
        for j in range(m):
            up = 0 if i - 1 < 0 else dp[i - 1][j]
            left = 0 if j - 1 < 0 else dp[i][j - 1]
            dp[i][j] = prob_mat[i][j] + max(left, up)
    
    print(dp)
    return dp[n - 1][m - 1]

matrix = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
print(solve(matrix))