
import pytest
from typing import List, Optional, Type


# The last word is the last set of characters
# there can be more whitespace after the last word

# Paste the LeetCode solution class here
class Solution:
    def lengthOfLastWord_Initial(self, s: str) -> int:
        word_len = 0
        whitespace_seen = 1

        lower_chars = [ord("a"), ord("z")]
        upper_chars = [ord("A"), ord("Z")]


        for char in s:
            char_digit = ord(char)

            # its a text char
            if lower_chars[0] <= char_digit <= lower_chars[1] or upper_chars[0] <= char_digit <= upper_chars[1]:
                if whitespace_seen:
                    word_len = 1
                    whitespace_seen = 0
                else:
                    word_len += 1
            # its whitespace
            else:
                whitespace_seen = 1

        return word_len


    def lengthOfLastWord(self, s: str) -> int:
        end_index = len(s) - 1
        idx = end_index
        count = 0

        while idx >= 0:
            # trailing space
            if s[idx] == " " and count == 0:
                pass
            # identified end of first word
            elif s[idx] == " " and count > 0:
                break
            # must be a char so count it
            else:
                count += 1

            idx -= 1

        return count


# Test cases
@pytest.mark.parametrize("x, expected", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("dogs are fruffy and noice", 5)
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.lengthOfLastWord_Initial(x) == expected
    assert solution.lengthOfLastWord(x) == expected
