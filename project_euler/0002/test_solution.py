import pytest

from typing import Optional


class Solution:
    def even_fib_num(self, lessx: int):
        fibs = [1, 2]

        # put first even fib into sum already
        fib_sum = 2

        next_fib = fibs[0] + fibs[1]
        fib_index = 3

        while next_fib < lessx:
            if next_fib % 2 == 0:
                fib_sum += next_fib
                print(f"Added another one: {next_fib} --> total: {fib_sum}")
            fibs.append(next_fib)
            next_fib = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]

        return fib_sum


@pytest.mark.parametrize(
    "lessx, expected",
    [
        (100, 44),
        (200, 188),
        (4_000_000, 1),  # final question
    ],
)
def test_solution(lessx, expected):
    solution = Solution()
    assert solution.even_fib_num(lessx) == expected
