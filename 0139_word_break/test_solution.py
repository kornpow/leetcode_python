
import pytest
from typing import List, Optional, Type

# check s[0], is it in word worddict?

# expandright on start char?
# catsandog

# find potential first word
# c -> f
# ca -> f
# cat -> t
# cats -> t

# cat
# s -> f
# sa -> f
# san -> f
# sand -> t

# cat sand
# o -> f
# og ->


# cats
# a -> f
# an -> f
# and -> t

# cats and
# o -> f
# og -> f

# Paste the LeetCode solution class here
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # print("Running wordBreak!")
        max_word_len = max([len(word) for word in wordDict])
        words_and_len = [(len(word),word) for word in wordDict]
        words_and_len.sort(reverse=True)
        print(words_and_len)
        # make a wordset from wordDict
        # since checking inclusivity in wordSet is O(1) where
        # checking inclusivity in wordList is O(N)
        wordSet = set(wordDict)
        strlen = len(s)
        # print(f"Longest word in list has max len: {max_word_len}")
        wordSet = set(wordDict)
        # print(f"Word: {s} -> wordlist: {wordSet}")

        memo = {}
        
        def expandOnIndex(start: int) -> bool:
            if start in memo:
                return memo[start]
            # exit condition, we made it all the way to the end of the
            # string with a chain of successful words
            if start == strlen:
                memo[start] = True
                return True


            
            i = 0
            # word = apple -> 0 + i = max_word_len -> s[0:i] =

            # check the largest possible word first and go down
            while i < len(words_and_len):
                next_word_len, word = words_and_len[i]

                if start + next_word_len > strlen:
                    i += 1
                    continue
                # we found a valid word in the window
                # start looking for the next word start at the next char
                check_word = s[start:start+next_word_len]
                # print(f"check_word: {check_word}")
                if check_word in wordSet:
                    # cats + andog
                    # print(f"Found a valid word: {check_word}")
                    if expandOnIndex(start+next_word_len):
                        memo[start] = True
                        return True
                i += 1

            # if the given start and all children starts are true, return false
            memo[start] = False
            return False

        return expandOnIndex(0)



    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        # DP: dp[i] says "is it possible to make a valid set of substrings...
        # from s[0:i], true or false
        dp = [False] * (n+1)

        dp[0] = True # empty string can always be segmented

        for i in range(1, n+1):
            for j in range(i):
                # check if dp has already been calculated to be true
                # 0->j is a valid string
                if dp[j]:
                    word = s[j:i]
                    if word in wordSet:
                        dp[i] = True
                        break
                    else:
                        pass
                else:
                    print(f"dp @ {j} is false, so impossible for dp @ {j}:{i} to be true")

        return dp[n]

# Test cases
@pytest.mark.parametrize("x, expected", [
    (("leetcode", ["leet","code"]), True),
    (("applepenapple", ["apple","pen", "aaaaaaaaa"]), True),
    (("catsandog", ["cats","dog","sand","and","cat"]), False),
    (("catsanddog", ["cats","dog","sand","and","cat"]), True),
    (("thiswontwork", ["this","won","work"]), False),
    (("thiswontwork", ["this","wont","work"]), True),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False),

])
def test_solution(x, expected):
    solution = Solution()
    assert solution.wordBreak(*x) == expected
    assert solution.wordBreakDP(*x) == expected
