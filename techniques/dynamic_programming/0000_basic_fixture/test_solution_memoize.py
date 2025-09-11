
import pytest
from typing import List, Optional, Type

##### PROBLEM STATEMENT #####
# Input: m = 3, n = 7
# Output: 28

# Input: m = 3, n = 2  
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Right -> Down  
# 3. Down -> Down -> Right

# ##### THOUGHTS #####
# m = 1
# n = 1

# (0,0) , memo = {}
# 0 = m-1 and 0 = n-1 ? NO!

# memo[(1,0)]

# dp

# [?,?,?]
# [?,?,?]
# [?,?,1]

# Paste the LeetCode solution class here
class Solution:
    def unique_paths_memoize(self, m: int, n: int):
        memo = {}

        def helper(row, col):
            # memo case
            if (row,col) in memo:
                return memo[(row,col)]

            # Base cases
            if row == m - 1 and col == n - 1:  # Reached destination
                # how can we cache this result?
                return 1
            if row >= m or col >= n:  # Out of bounds
                return 0
            
            result = helper(row + 1, col) + helper(row, col + 1)
            memo[(row,col)] = result
            return result
        
        return helper(0, 0)


    def unique_paths_naive(self, m: int, n: int):
        """
        Naive recursive solution - VERY SLOW for large inputs
        """
        def helper(row, col):
            # Base cases
            if row == m - 1 and col == n - 1:  # Reached destination
                return 1
            if row >= m or col >= n:  # Out of bounds
                return 0
            
            # Recursive case: try going right OR down
            return helper(row + 1, col) + helper(row, col + 1)
        
        return helper(0, 0)

    def unique_paths_dp(self, m: int, n: int):
        """
        Dynamic Programming Solution
        Work Forwards to the end

        """  

        # dp holds number of moves to get to current position
        dp = [ [ 0 for a in range(0,m) ] for b in range(0,n) ]
        # dp[y-axis][x-axis]


        for i in range(1, m):
            dp[0][i] = dp[0][i-1] + 1

        for z in range(1, n):
            dp[z][0] = dp[z-1][0] + 1

        for i in range(1,m):
            for z in range(1, n):
                print(z,i)
                # to get to i,z you need to sum number of way to get to 1 to the left and 1 up
                dp[z][i] = dp[z-1][i] + dp[z][i-1]
                

        for row in dp:
            print(row)

        return dp[n-1][m-1]



# Test cases
@pytest.mark.parametrize("m, n, expected", [
    # (1, 1, 1),
    (3, 3, 8),
    (2, 2, 2),
    (2, 1, 1),
    # (),
])
def test_solution(m, n, expected):
    solution = Solution()
    assert solution.unique_paths_naive(m, n) == expected
    assert solution.unique_paths_memoize(m, n) == expected
    assert solution.unique_paths_dp(m, n) == expected


