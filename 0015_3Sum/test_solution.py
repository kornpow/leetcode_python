
import pytest
from typing import List, Optional, Type


# Basically all this problem is saying is that we need 3 different indexes, i,j,k
# and summing the values at those indexes==0

# unless there are 3 0's, there has to be either 2 positive and 1 neg
# OR 2 neg and 1 pos

# [-1,0,1,2,-1,-4]
# SORT THEM!
# [-4, -1, -1, 0, 1, 2]
# choose X1 = -4
# left: [-1,-1]
# middle: [0]
# right: [1, 2]

# if SUM1 < 0:
#     choose biggest number

# [-4 , 2]
# # choose X2 = 2
# # left: [-1,-1]
# # middle: [0]
# # right: [1]

# SUM2 = X1 + X2

# if SUM2 < 0:
#      choose X3 = largest number

# SUM1 = X1 + X2 + X3

# if SUM3 < 0:
#     # then it is impossible for X1 to ever successfully sum to 0
#     # therefore drop it

# START_LIST = [-1, -1, 0, 1, 2]

# X1 = Smallest number = -1
# SUM1 = X1

# if X1 < 0
# if SUM1 < 0:
#     choose biggest number

# [-1,0,1,2]
# X2 = 2
# SUM2 = X1 + X2 = -1 + 2 = 1

# if SUM2 > 1:
#     Choose smallest number

# [-1,0,1]

# X3 = -1
# SUM3 = -1 + 2 + -1 = 0
# SUCCESS! add [-1,2,-1] to final

# DROP X1 again???

# START_LIST = [-1, 0, 1, 2]

# X1 = -1
# SUM1 = -1

# X2 = 2
# SUM2 = -1 + 2 = 1

# CHOOSE SMALLEST

# X3 = 0
# SUM3 = -1 + 2 + 0 = 1

# DROP LARGEST

# START_LIST = [-1, 0, 1]






# Paste the LeetCode solution class here
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        found_list = []

        start_list = sorted(nums)

        while len(start_list) > 3:
            working_list = start_list[:]
            print(f"WORKING LIST: {working_list}")
            # choose smallest
            X1 = working_list.pop(0)
            SUM1 = X1
            
            if SUM1 < 0:
                X2 = working_list.pop()
            elif SUM1 > 0:
                X2 = working_list.pop(0)
            else:
                # shortcut?
                X2 = working_list.pop()

            SUM2 = SUM1 + X2

            if SUM2 < 0:
                # get biggest
                X3 = working_list.pop()
            elif SUM2 > 0:
                # get smallest
                X3 = working_list.pop(0)
            else:
                # get biggest
                X3 = working_list.pop()

            SUM3 = SUM2 + X3

            # modify the original list to eliminate infinite loops
            if SUM3 < 0:
                # get biggest
                print("Pop Smallest")
                start_list.pop(0)
            elif SUM3 > 0:
                # get smallest
                print("Pop Biggest")
                start_list.pop()
            else:
                print("Pop Smallest")
                start_list.pop()
                # get biggest
                found_list.append([X1,X2,X3])

        # print(partials)
        return found_list


# Test cases
@pytest.mark.parametrize("x, expected", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
    ([-2,-4,6,0,-1,1], [[-2,-4,6],[0,-1,1]]),
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.threeSum(x) == expected
