
import pytest
from typing import List, Optional, Type

# Question 1
# Sum of natural numbers below n, which are multiples of 3 and 5
# Paste the LeetCode solution class here
class Solution:
    def natural_sum(self, x: int) -> bool:
        final_sum = 0

        for i in range(0, x):
            if i % 3 == 0:
                final_sum += i
            elif i % 5 == 0:
                final_sum += i

        return final_sum



# Test cases
@pytest.mark.parametrize("x, expected", [
    (10, 23),
    (12, 33),
    (13, 45),
    (15, 45),
    (16, 60),
    (1000, 233168),
    # (10, True),
    # (101, True),
    # (101000, True),
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.natural_sum(x) == expected
