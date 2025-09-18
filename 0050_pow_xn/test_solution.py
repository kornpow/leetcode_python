import pytest

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Either x is not zero or n > 0. -> x != 0 OR n > 0

# 2 ^ 5 = 2 * 2 * 2 * 2 * 2


# TIME: O(n)
# SPACE: O(1)
# Paste the LeetCode solution class here
class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     # initial check??
    #     if not (x == 0 and n <= 0):
    #         pass

    #     # simpler way to describe negative exponents
    #     if n < 0:
    #         x = 1/x
    #         n = abs(n)

    #     result = 1
    #     for i in range(0, n):
    #         result = result * x
    #         if x < 1 and abs(result) < 0.00001:
    #             return 0
    #         # print(result)

    #     return round(result,5)

    # recursion?
    # x^4 = x^3 * x => x^n = x ^ n-1

    # x^n = [0,0,0,0,0]

    # x*x*x*x
    # x^2 = x*x
    # x^3 = x * x^2
    # x^4 = x^2 * x^2
    # x^5 = x * x^4

    # 4^10 -> 2^2
    # n = 5
    # its odd
    # divmod(n,2)

    # TODO: someday reimplement using recursive binary exponentiation
    # TIME: O(log n)
    # SPACE: O(log n)
    def myPow(self, x: float, n: int) -> float:
        memo = {}

        def power_recursive(x: float, n: int) -> float:
            if n in memo:
                return memo[n]

            if n == 0:
                memo[n] = 1
                return memo[n]

            if n == 1:
                memo[n] = x
                return memo[n]

            if n < 0:
                x = 1 / x
                n = abs(n)

            is_even = bool(n % 2) == 0

            if is_even:
                # 2^4 = 2^2 * 2^2
                result = power_recursive(x, n // 2) * power_recursive(x, n // 2)
                memo[n] = result
                return memo[n]
            else:
                # 2^3 = 2^2 * 2^1
                divmod(n, 2)
                result = power_recursive(x, n - 1) * power_recursive(x, 1)
                memo[n] = result
                return memo[n]

        result = power_recursive(x, n)
        # print(calcs)
        return round(result, 8)


# Test cases
@pytest.mark.parametrize(
    "x, n, expected",
    [
        (2.00000, 10, 1024.00000),
        (2.10000, 3, 9.26100),
        (2.00000, -2, 0.25000),
        (0.00001, 2147483647, 0),
    ],
)
def test_solution(x, n, expected):
    solution = Solution()
    assert solution.myPow(x, n) == expected
