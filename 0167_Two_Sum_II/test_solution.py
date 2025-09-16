import pytest
from typing import List, Optional, Type


# 1 indexed, for some reason, just add one at the end?


# Paste the LeetCode solution class here
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 1
        ptr2 = len(numbers)

        # add a dummy to make it 1 indexed
        numbers.insert(0, 0)
        atarget = None
        while ptr1 < ptr2:
            asum = numbers[ptr1] + numbers[ptr2]
            if asum == target:
                return [ptr1, ptr2]
            if asum < target:
                ptr1 += 1

            if asum > target:
                ptr2 -= 1


# Test cases
@pytest.mark.parametrize(
    "x, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_solution(x, target, expected):
    solution = Solution()
    assert solution.twoSum(x, target) == expected
