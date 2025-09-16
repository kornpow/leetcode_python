import pytest


class Solution:
    def test_rotting_oranges(self, x):
        pass


@pytest.mark.parametrize("x, expected", [("", "")])
def test_solution(x, expected):
    solution = Solution()

    assert solution.test_rotting_oranges(x) == expected
