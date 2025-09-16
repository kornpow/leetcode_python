import pytest
from typing import List, Optional, Type


# Paste the LeetCode solution class here
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # set to max_length string could be
        min_len = 201
        for a in strs:
            if len(a) < min_len:
                min_len = len(a)

        # if any word is blank than thats the longest prefix
        if "" in strs:
            return ""

        longest_prefix = ""
        i = 0
        while i < min_len:
            next_char_set = set()
            for word in strs:
                next_char_set.add(word[i])

            # Common char at index
            if len(next_char_set) == 1:
                char = next_char_set.pop()
                longest_prefix += char
                i += 1
                continue
            # more than 1 chars at index
            break

        return longest_prefix


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["cat", "car", ""], ""),
        (["lamb", "lamp", "lamps"], "lam"),
        (["bam", "bambi", "bambino"], "bam"),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.longestCommonPrefix(x) == expected
