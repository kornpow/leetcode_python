from typing import List

import pytest

# variables to keep track of:
# current_path: List[str]
# remaining_digits: List[str]

# initial dfs:
# dfs([], digits_list)

letter_map = {
    "2": list("abc"),
    "3": list("def"),
    "4": list("ghi"),
    "5": list("jkl"),
    "6": list("mno"),
    "7": list("pqrs"),
    "8": list("tuv"),
    "9": list("wxyz"),
}


# Paste the LeetCode solution class here
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_list = list(digits)

        if digits == "":
            return []

        result_count = 1
        print("")
        for digi in digits_list:
            result_count *= len(letter_map[digi])

        print(f"the answer will have: {result_count} combinations!")

        solutions = []

        def dfs(path: List[str], remaining_digits: List[str]) -> None:
            if len(remaining_digits) == 0:
                solutions.append("".join(path))
                return
            next_digit = remaining_digits[0]
            possible_next_chars = letter_map[next_digit]
            for char in possible_next_chars:
                dfs(path + [char], remaining_digits[1:])

            return

        dfs([], digits_list)

        print(f"Does the result match expected? ->> {len(solutions)==result_count}")

        return solutions


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        ("9", ["w", "x", "y", "z"]),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.letterCombinations(x) == expected
