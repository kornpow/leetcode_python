from typing import List

import pytest

# remove duplicate numbers from sorted list (IN PLACE) and
# return the number of unique numbers

# need to modify list in place, so use pop(index)


# Paste the LeetCode solution class here
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # print(f"Original List: {nums}")
        n = len(nums)
        i = 0
        # [1,1,2,2], n = 4, order
        delete_index = []
        while i < n - 2:
            # if next one is same as this one
            # pop off this one
            if nums[i + 1] == nums[i]:
                delete_index.append(i)

            i += 1

        # print(f"Delete these! --> {delete_index}")
        for z in range(len(delete_index) - 1, -1, -1):
            print(z)
            nums.pop(delete_index[z])

        return len(nums)

    def removeDuplicates_faster(self, nums: List[int]) -> int:
        # print(f"Original List: {nums}")
        n = len(nums)
        # i = 0
        # [1,1,2,2], n = 4, order
        i = n - 1
        # iterate from the end to the beginning
        # always pop off from the end so as to not mess with our indexes
        while i > 0:
            # if next one is same as this one
            # pop off this one
            if nums[i - 1] == nums[i]:
                nums.pop(i)

            i -= 1

        return len(nums)

    def removeDuplicates_final(self, nums: List[int]) -> int:
        # we dont need to pop() the values off the list
        # we just need to reorder so that the first k elements are unique
        # and then return k

        # The first possible duplicate is idx 1, idx 0 is always unique
        # Instead of thinking of finding duplicates, think about writing unique
        # values to write_idx
        write_idx = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[write_idx - 1]:
                # Dont update write_idx because its not a unique value
                pass
            elif nums[i] != nums[write_idx - 1]:
                nums[write_idx] = nums[i]
                write_idx += 1

        return write_idx


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ],
)
def test_solution(x, expected):
    solution = Solution()

    # result_count1 = solution.removeDuplicates(x)
    # result_count2 = solution.removeDuplicates_faster(x)
    result_count3 = solution.removeDuplicates_final(x)

    # assert result_count1 == len(expected)
    # assert result_count2 == len(expected)
    assert result_count3 == len(expected)

    for i in range(0, result_count3):
        assert x[i] == expected[i]
