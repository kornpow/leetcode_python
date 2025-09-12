import pytest

# 10 -> 

class Solution:
    def is_prime(self, x: int) -> bool:
        if x < 2:
            return False

        return False

    def largest_prime_factor(self, x: int):
        pass


@pytest.mark.parametrize("x, expected",[
    (10, 5),
])
def test_solution(x, expected):
    solution = Solution()

    assert solution.largest_prime_factor(x) == expected