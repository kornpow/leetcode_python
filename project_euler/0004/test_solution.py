import pytest


# largest palidrome of two digit numbers is: 9009 = 91 * 99
# largest product of two digit numbers is: 99*99 = 9801
# largest product of three digit numbers: 999*999 = 998001
# smallest product of three digit numbers: 100*100= 10_000
# find first palindromes number <= 998001


class Solution:
    def is_palindrome_num(self, num: int) -> bool:
        num_string = str(num)
        # use integer division since the middle char doesnt matter
        compare_len = len(num_string) // 2

        if num_string[0:compare_len] == num_string[-compare_len:][::-1]:
            return True
        return False

    def largest_palindrome_product(self, x: int) -> int:
        smallest_factor = 1
        for i in range(1, x):
            smallest_factor *= 10

        largest_factor = int("".join(["9" for i in range(0, x)]))

        print(f"smallest factor: {smallest_factor}")
        print(f"largest factor: {largest_factor}")

        smallest_product = smallest_factor * smallest_factor
        largest_product = largest_factor * largest_factor
        print(f"smallest product: {smallest_product}")
        print(f"largest product: {largest_product}")

        largest_product = 0
        # 999 * 999 -> 999*998
        for y in range(largest_factor, smallest_factor - 1, -1):
            for z in range(largest_factor, smallest_factor - 1, -1):
                product = y * z
                if self.is_palindrome_num(product):
                    largest_product = max(product, largest_product)

        return largest_product


@pytest.mark.parametrize(
    "x, expected",
    [
        (2, 9009),
        (3, 906609),
        (4, 99000099),
    ],
)
def test_largest_palindrome_product(x, expected):
    solution = Solution()
    assert solution.largest_palindrome_product(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (1001, True),
        (1000, False),
        (12321, True),
        (123321, True),
        (123421, False),
    ],
)
def test_is_palindrome(x, expected):
    solution = Solution()
    assert solution.is_palindrome_num(x) == expected
