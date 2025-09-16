import pytest
from typing import List, Optional, Type

# what is fibonacci?
# 1 + 1 = 2 + 1 = 3 + 2 = 5 + 3
#  f_n = f_(n-1) + f_(n-2)


# Paste the LeetCode solution class here
class Solution:
    def fibonacci(self, x: int) -> int:
        calculated_fib = [None for i in range(0, x + 1)]
        calculated_fib[0] = 0
        calculated_fib[1] = 1

        def fib(n):
            if calculated_fib[n - 1] != None:
                print("Use cache")
                n_1 = calculated_fib[n - 1]
            else:
                n_1 = fib(n - 1)

            if calculated_fib[n - 2] != None:
                print("Use cache")
                n_2 = calculated_fib[n - 2]
            else:
                n_2 = fib(n - 2)

            calculated_fib[n] = n_1 + n_2
            print(calculated_fib)
            return calculated_fib[n]

        return fib(x)


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        (2, 1),
        (3, 2),
        (4, 3),
        (19, 4181),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.fibonacci(x) == expected
