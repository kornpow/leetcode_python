
import pytest
from typing import List, Optional, Type

# abcabcbb -> 3
# create list of ints of the length of the string
# [0,0,0,0,0,0,0...]
# start from index 0
# expand right from index 0
# dp[n] = dp[n-1] + 1 if s[n-1] != s[n] else 1

# [       {},{b}]


# Paste the LeetCode solution class here
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(f"Find longest substring in string: {s}")
        # DP[i] holds longest substring starting
        # at index i
        if s == "":
            return 0
        dp = [0] * len(s)

        print(len(dp) == len(s))

        # O(N)
        for i in range(len(s)):
            count = 0
            # O(N)
            for j in range(i+1,len(s)+1):
                # allocate string
                test_string = s[i:j]
                # print(f"Test string: {test_string}")
                # unique chars == total chars
                # O(1)
                if len(set(test_string)) == len(test_string):
                    count += 1
                else:
                    break

            dp[i] = count

        print(dp)
        return max(dp)

    def lengthOfLongestSubstring_On(self, s: str) -> int:
        ans = 0
        n = len(s)

        # mp stores the current index of a character
        mp = {}
        
        #
        start_index = 0
        for end_index in range(n):
            if s[end_index] in mp:
                # we have seen this character before
                # increment the start index to be the max
                # of the previous last seen and the current
                start_index = max(start_index, mp[s[end_index]])
                
            ans = max(ans, end_index-start_index+1)
            mp[s[end_index]] = end_index + 1

        return ans

# Test cases
@pytest.mark.parametrize("x, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(x) == expected
    assert solution.lengthOfLongestSubstring_On(x) == expected
