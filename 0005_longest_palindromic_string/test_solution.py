
import pytest

# "abab"
# brute force? get all substrings and then detect palindrome


# s = "abab":
# check 4 chars - s[0:0+4]

# Paste the LeetCode solution class here
class Solution:
    def is_palindrome(self, s: str) -> bool:
        len_str = len(s)
        if len_str == 1:
            return True

        # integer division half, since if odd, middle char doesnt matter
        half = len(s) // 2
        print()
        if s[0:half] == s[-half:][::-1]:
            return True
        else:
            return False

    def longestPalindrome_bruteforce(self, s: str) -> str:
        max_len = len(s)
        longest_palindrome_str = ""
        # longest_palindrome_len = 0

        for i in range(0,max_len):
            for z in range(1, max_len+1):
                test_str = s[i:z]
                
                if self.is_palindrome(test_str):
                    if len(test_str) > len(longest_palindrome_str):
                        longest_palindrome_str = test_str
                        print(f"new longest palindrome: {longest_palindrome_str}")
                        # special case, end early
                        if len(longest_palindrome_str) == len(s):
                            return longest_palindrome_str
        
        return longest_palindrome_str

    def longestPalindrome(self, s: str) -> str:
        # longest potential substring is the entire string
        potential_max = len(s)
        # print(f"max substring len: {potential_max} -> {s[0:potential_max]}")

        check_len = potential_max
        # start from the biggest possible and work down
        for i in range(check_len,0,-1):
            start_idx = 0
            while start_idx+check_len <= potential_max:
                test_str = s[start_idx:start_idx+check_len]
                if self.is_palindrome(test_str):
                    return test_str
                start_idx += 1

            # didnt find a palindrome in last loop, check for 1 smaller next
            check_len -= 1

        return ""




# Test cases
@pytest.mark.parametrize("x, expected", [
    ("babad", "bab"),
    ("testtset", "testtset"),
    ("1", "1"),

])
def test_solution(x, expected):
    solution = Solution()
    # assert solution.longestPalindrome_bruteforce(x) == expected
    assert solution.longestPalindrome(x) == expected

@pytest.mark.parametrize("x, expected", [
    ("babab", True),
    ("testtset", True),
    ("1234", False),
    ("1", True),
    ("xyzabc", False),
    ("dohreighmeefahsolahtido", False),
])
def test_solution2(x, expected):
    solution = Solution()
    assert solution.is_palindrome(x) == expected