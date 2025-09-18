from typing import List

import pytest

# 3SUM we need to return VALUES, in 2SUM we are return INDEXES to Values


# Paste the LeetCode solution class here
class Solution:
    def threeSum_take1(self, nums: List[int]) -> List[List[int]]:
        # print(f"3SUM:\n{nums}")
        solution = []
        n = len(nums)
        # create a map which swaps value for index
        num_map = {}
        solution_map = {}
        for i, val in enumerate(nums):
            num_map[val] = i

        # print(f"NUM MAP: {num_map}")

        # n1 is an index
        # O(N)
        for n1 in range(n - 1):
            # n2 is an index
            # O(N)
            for n2 in range(1, n):
                # indexes CANT be the same
                if n1 == n2:
                    continue

                # ht is a number
                ht = nums[n2] + nums[n1]
                # print(f"Sum of first two numers: {ht}")
                ht_inverse = -ht
                # print(f"Find the inverse number in the num_map: {ht_inverse}")

                # O(1)
                if ht_inverse in num_map:
                    # check that it doesnt repeat one of the first two
                    if num_map[ht_inverse] == n2 or num_map[ht_inverse] == n1:
                        continue

                    n3 = num_map[ht_inverse]
                    # print(f"found a triplet! {n1} {n2} {n3}")
                    # print(f"Total sum: {nums[n3] + nums[n1] + nums[n2]}")
                    tempresult = [nums[n3], nums[n1], nums[n2]]
                    # tempresult.sort()
                    # result_marker = f"{n1}:{n2}:{n3}"
                    result_marker = n1 + n2 + n3
                    if result_marker not in solution_map:
                        solution_map[result_marker] = 1
                        solution.append(tempresult)

        # print("A SOLUTION!")
        # print(solution_map)
        # print(solution)
        return solution

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # print(f"3SUM: {nums}")
        # print(nums)
        nums.sort()
        # print(nums)
        results = []
        last_num = float("inf")
        for pivot, val in enumerate(nums):
            if val == last_num:
                # last_num = val
                continue

            last_num = val

            # sorted list so if the first number is > 0 then none of the rest can be less than 0
            if val > 0:
                break
            start_index = pivot + 1
            end_index = n - 1

            while start_index < end_index:
                # reached the end
                if start_index == n - 1:
                    break

                result = [val, nums[start_index], nums[end_index]]
                print(result)
                try:
                    sum3 = sum(result)
                except IndexError as e:
                    # print(f"error at : {start_index}")
                    raise e

                # print(f"Sum of all three: {sum3}")
                if sum3 == 0:
                    # result.sort()
                    # if result not in results:
                    print(f"append: {result}")
                    results.append(result)

                    # Skip duplicates for start_index
                    while start_index < end_index and nums[start_index] == nums[start_index + 1]:
                        start_index += 1
                    # Skip duplicates for end_index
                    while start_index < end_index and nums[end_index] == nums[end_index - 1]:
                        end_index -= 1

                    start_index += 1
                    end_index -= 1

                elif sum3 > 0:
                    end_index -= 1
                else:
                    start_index += 1

        print(results)
        return results


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, -4, 6, 0, -1, 1], [[-2, -4, 6], [0, -1, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_solution(x, expected):
    solution = Solution()

    result2 = solution.threeSum(x)
    for sol in expected:
        assert list(sorted(sol)) in list(sorted(result2))

    # initial run with our brute force approach
    # result = solution.threeSum_take1(x)
    # for sol in expected:
    #     assert sol in result
