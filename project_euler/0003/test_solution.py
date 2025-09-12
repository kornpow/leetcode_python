import pytest
import math
# 10 -> 

class Solution:
    def is_prime(self, x: int) -> bool:
        """
        Primes are numbers which can only be divisible by itself and 1
        """
        if x < 2:
            return False
        elif x == 2:
            return True
        elif x > 2:
            for i in range(3, x):
                div, remainder = divmod(x,i)
                # another divisor which isnt itself
                if remainder == 0:
                    print(f"Found another divisor -> {i}")
                    return False

        return True

    def largest_prime_factor(self, x: int):
        prime_factors = []

        # check if divisible by 2, if it is, do it
        if x % 2 == 0:
            prime_factors.append(2)
            x = x / 2


        i = 3
        while i*i <= x:
            if x % i == 0:
                x = x/i
                prime_factors.append(i)
            i += 1

        
        if x > 1:
            prime_factors.append(x)

        print(f"All Prime factors: {prime_factors}")
        return max(prime_factors)
        


@pytest.mark.parametrize("x, expected",[
    (10, False),
    (11, True),
    (99, False),
    (91, False),
    (97, True),
])
def test_is_prime(x, expected):
    solution = Solution()

    assert solution.is_prime(x) == expected


@pytest.mark.parametrize("x, expected",[
    (7, 7),
    (13195, 29),
    (600851475143, 6857),
])
def test_largest_prime_factor(x, expected):
    solution = Solution()

    assert solution.largest_prime_factor(x) == expected