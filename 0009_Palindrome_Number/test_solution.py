
import pytest

# Paste the LeetCode solution class here
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

# Test cases
@pytest.mark.parametrize("x, expected", [
    (121, True),
    (-121, False),
    (10, False),
    (-101, False),
])
def test_is_palindrome(x, expected):
    solution = Solution()
    assert solution.isPalindrome(x) == expected
