
import pytest
from typing import List, Optional, Type

# how to algorithmically figure this out???
# "1100011000",
# "0101001010"
# XOR IT
# "1001010010"


# it is impossible to swap our way to success
# if there is unequal number of 1s.. WRONG?
# NOT unequal number, but odd vs even

# There has to be a limit where next2 swapping multiple times is cheaper than any2 swapping

# 1: 10110
# 2: 00011
# X: 10101

# 1: 01110
# 2: 00011
# X: 01101

# 1: 00010
# 2: 00011
# X: 00001


# S 1001010010
# = 0101010010  cost 1
# = 0011010010  cost 1
# = 0000010010  cost 1
# = 0000001010  cost 1
# = 0000000110  cost 1
# = 0000000000  cost 1
# total cost = 6 using only next2 swaps

# find number of zeros between 1s
# 2 1 2
# cost of any2 swap = 2 next2 = 1
# => if num zeros > (cost_any2 - 1) its cheaper to do any2





# Paste the LeetCode solution class here
class Solution:
    # flip both s1[i] and s1[j]
    # costs x
    def op_flip_any2(self, s: str, i: int, j: int) -> str:
        s = list(s)
        ti = s[i]
        tj = s[j]

        s[i] = "1" if s[i] == "0" else "0"
        s[j] = "1" if s[j] == "0" else "0"

        return "".join(s)
    
    # costs 1
    def op_flip_next2(self, s: str, i: int) -> str:
        s = list(s)

        s[i] = "1" if s[i] == "0" else "0"
        s[i+1] = "1" if s[i+1] == "0" else "0"

        return "".join(s)



    def minOperations(self, s1: str, s2: str, x: int) -> int:
        print("Running minOperations!")

        xor = []
        count1s_1 = 0
        count1s_2 = 0
        distance = []
        last_one_pos = None
        for i in range(0,len(s1)):
            if s1[i] == "1":
                count1s_1 += 1
            if s2[i] == "1":
                count1s_2 += 1
            matches = "0" if s1[i]==s2[i] else "1"
            if matches == "1":
                if last_one_pos is not None:
                    distance.append(i-last_one_pos-1)
                last_one_pos = i
            xor.append(matches)
            print(f"Index {i}:  {s1[i]==s2[i]}")

        print("".join(xor))

        # if one has odd and other has even we cant do it
        if count1s_1 % 2 != count1s_2 % 2:
            return -1

        print(distance)

        num_ops = len(distance) - 1
        num_next2 = 0
        num_any2 = 0
        for x, val in enumerate(distance):
            print(x,val)
            if val < x:
                num_next2 += 1

        num_any2 = num_ops - num_next2
        cost = x * num_any2 + num_next2
        return cost


        

# Test cases
@pytest.mark.parametrize("s1, s2, x, expected", [
    ("1100011000","0101001010", 2, 4),
    ("10110", "00011", 4, -1),
    ("00010", "00011", 4, -1),
    ("101101", "000000", 6, 4),
])
def test_solution(s1, s2, x, expected):
    solution = Solution()
    assert solution.minOperations(s1, s2, x) == expected
