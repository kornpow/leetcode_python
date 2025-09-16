import pytest
from typing import List, Optional, Type

import string

# Types of numbers
# integers + exponent
# decimal + exponent

# and exponent is an e/E followed by integer number

# determine if there is an exponent in the string
# isDecimal: determine if there is a dot in the string


# Paste the LeetCode solution class here
class Solution:
    def checkSign(self, test: str):
        num_signs = 0
        unsigned_test = list(test)

        num_signs = unsigned_test.count("+") + unsigned_test.count("-")

        # check for signs in the middle
        if num_signs > 0:
            if unsigned_test[0] not in ["+", "-"]:
                return False, test

        test = test.replace("+", "").replace("-", "")
        # print(f"Cleaned number: {test}")
        return num_signs < 2, test

    def isDecimal(self, test: str):
        good_sign, cleaned = self.checkSign(test)
        if not good_sign:
            return False

        # print(f"Len cleaned: {len(cleaned)}")
        # min decimal value
        if len(cleaned) < 2:
            return False

        # only a single decimal place valid
        if cleaned.count(".") > 1:
            return False

        return True

    def isInteger(self, test: str):
        good_sign, cleaned = self.checkSign(test)
        if not good_sign:
            return False

        if len(cleaned) < 1:
            return False

        # ints have no decimal place
        if "." in cleaned:
            return False

        return True

    def isNumber(self, s: str) -> bool:
        # print(f"\nisNumber: {s}")
        s = s.lower()
        invalid_chars = list(string.ascii_lowercase)
        # print(invalid_chars)

        invalid_chars.remove("e")
        # print(invalid_chars)

        for char in s:
            if char in invalid_chars:
                return False

        if s.count("e") > 1:
            return False
        elif "e" in s:
            # print("Has exponent")
            main, expo = s.split("e")
            # print(main,expo)

            if not self.isInteger(expo):
                return False
        else:
            main = s

        # determine if main is decimal or int

        if "." in main:
            # print(f"Test For decimal validity: {main}")
            if self.isDecimal(main):
                return True
            else:
                return False
        else:
            if self.isInteger(main):
                return True
            else:
                return False


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        ("0", True),
        ("e", False),
        (".", False),
        ("101.", True),
        ("10e7", True),
        ("10e7", True),
        ("10e-7", True),
        (".10e-7", True),
        (".10.e-7", False),
        (".10e-7.", False),
        ("-.E3", False),
        ("ee", False),
        ("inf", False),
        ("-inf", False),
        ("6+1", False),
        ("4e+", False),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.isNumber(x) == expected
