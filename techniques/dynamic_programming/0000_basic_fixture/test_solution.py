
import pytest
from typing import List, Optional, Type


# Paste the LeetCode solution class here
class Solution:
    def find_change(self, coins: List[int], amount: int):
        dp = [float("inf")] * (amount + 1)
        # base case, takes 0 coins to make 0
        dp[0] = 0
        print(dp)

        # calculate up to amount
        for i in range(1, amount+1):
            for coin in coins:
                # case 1: can make the value with single coin
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
@pytest.mark.parametrize("coins, x, expected", [
    ([1,2,3], 6, 2),
    ([1,2,3], 8, 3),
    ([1,2,4], 3, 2),
])
def test_solution(coins, x, expected):
    solution = Solution()
    assert solution.find_change(coins, x) == expected
