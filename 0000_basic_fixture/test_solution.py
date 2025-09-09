
import pytest
from typing import List, Optional, Type


# Paste the LeetCode solution class here
class Solution:
    def isPositive(self, x: int) -> bool:
        if x <= 0:
            return False
        return True


# Test cases
@pytest.mark.parametrize("x, expected", [
    (-1, False),
    (0, False),
    (10, True),
    (101, True),
    (101000, True),
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.isPositive(x) == expected
