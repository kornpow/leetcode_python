
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

    def is_palindrome2(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True


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


    def longestPalindrome_on2(self, s: str) -> str:
        # palindrome length = 1 is initial longest
        longest_pal = s[0]
        max_len = len(s)

        # use an internal function so we dont need to pass in shared variables
        def expandFromCenter(left: int, right: int) -> (str, int):
            """
            if odd -> right - left = 2
            if even -> right - left = 1

            check even, 2 abba -> a -> left = a,0 , right = b,1
            check odd, 3 abba -> a -> left = a,0 , right = b,2

            """
        
            while left >= 0 and right < max_len:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break

            # both left/right get incremented one extra, and then fails
            # so a typical length of r-l +1 -2 = r-l-1
            palindrome_length = right - left - 1
            palindrome_string = s[left+1:right]


            print(f"Found palindrome -> {palindrome_string}, with length: {palindrome_length}")
            # return palindrome, length of palindrome
            return palindrome_string, palindrome_length

        
        for i in range(max_len):
            # 1,3,5,7
            # i,i since 1char palindrome exists
            pal_odd_str, pal_odd_len = expandFromCenter(i,i)
            # 2, 4
            # i,i+2 since checks equality of i and i+1 initial
            # palidrome of length 2, 4
            pal_even_str, pal_even_len = expandFromCenter(i,i+1)
            print(pal_even_str, pal_odd_str)
            current_len, current_pal = max((pal_odd_len, pal_odd_str),(pal_even_len, pal_even_str))

            if current_len > len(longest_pal):
                print(f"New longest: {longest_pal}")
                longest_pal = current_pal

        return longest_pal



# Test cases
@pytest.mark.parametrize("x, expected", [
    ("babad", "bab"),
    ("testtset", "testtset"),
    ("1", "1"),
    ("cbbd", "bb")
])
def test_solution(x, expected):
    solution = Solution()
    assert solution.longestPalindrome_bruteforce(x) == expected
    assert solution.longestPalindrome(x) == expected
    assert solution.longestPalindrome_on2(x) == expected

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
    assert solution.is_palindrome2(x) == expected