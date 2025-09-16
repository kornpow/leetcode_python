import pytest

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000


# (IV) 4
# (IX) 9
# (XL) 40
# (XC) 90
# (CD) 400
# (CM) 900

# divmod(3749,1000) = 3, 7490
# subtract value
# add roman numeral to result: "M"

# divmod(2749,1000) = 2, 7490
# subtract value
# add roman numeral to result: "MM"

# divmod(1749,1000) = 3, 7490
# subtract value
# add roman numeral to result: "MMM"

# v, r = divmod(749,1000) = 0, 7490
# if v == 0: move to next largest numeral -> 900

# v, r = divmod(749,500) = 1, 249
# if v > 0:
# subtract value: 749 - 500
# add roman numeral to result: "MMMD"

numeral_map = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


# Paste the LeetCode solution class here
class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        for numeral_val in numeral_map:
            v = 1
            while v > 0:
                v, r = divmod(num, numeral_val)
                print(f"num: {num}, v: {v}, r: {r}")
                if v > 0:
                    num = num - numeral_val
                    result.append(numeral_map[numeral_val])

        print(result)
        return "".join(result)


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.intToRoman(x) == expected
