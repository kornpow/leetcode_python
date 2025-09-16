
import pytest
from typing import List, Optional, Type

# PROBLEM
# given a list of integers
# return the two indexes whose integers sum up to the `target`

# SOLUTION
# Instead of trying to use the list and do addition there
# make a dictionary which has the integer as key and index as the value
# that way we can use O(1) lookups of keys instead of O(n) iterations on a list

### HMM THIS DOESNT WORK
# THE ISSUE IS RELATED TO

# SET:
# 

# Paste the LeetCode solution class here
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSum_On2(nums, target)


    def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
        numnums = len(nums)
        for i in range(numnums-1):
            for j in range(1,numnums):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return (i,j)

    def twoSum_On(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                if i < num_dict[complement]: return (i, num_dict[complement])
                else: return (num_dict[complement], i)
            num_dict[num] = i

# Test cases
@pytest.mark.parametrize("x, expected", [
    (([2, 7, 11, 15], 9), (0,1)),
    (([3, 2, 4], 6), (1,2)),
    (([3, 3], 6), (0,1)),
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.twoSum_On(*x) == expected
    assert solution.twoSum_On2(*x) == expected
