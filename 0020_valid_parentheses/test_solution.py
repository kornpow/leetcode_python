import pytest

# use a stack?
# get character
# check if opening or closing
# if opening add to the stack
# if closing, check if last element on the stack == closing complement
# if yes: pop element from stack
# if no: return false


# ([)] -> open, open, close, close
# [ "(", "[" ]

openings = {
    "{": "}",
    "(": ")",
    "[": "]",
}

closings = {
    "}": "{",
    ")": "(",
    "]": "[",
}


# Paste the LeetCode solution class here
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in closings:
                if len(stack) == 0:
                    return False
                if closings[char] != stack[-1]:
                    return False
                else:
                    stack.pop()

            if char in openings:
                stack.append(char)

        # left over opening chars
        if len(stack) > 0:
            return False

        return True


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        ("()", True),
        ("((", False),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.isValid(x) == expected
