from typing import Optional

import pytest


# Paste the LeetCode solution class here
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# n = 2 -> remove second to last
# n = 1 -> remove last


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        heads = []
        while node is not None:
            print(node.val)
            heads.append(node)
            node = node.next

        list_len = len(heads)
        if n == 1 and list_len > 1:
            print(f"n: {n} -> list_len: {list_len}")
            heads[-2].next = None
        elif n == 1 and list_len == 1:
            return None
        # drop the first one
        elif n == list_len:
            head = heads[1]
        else:
            # heads[-1] -> last
            # heads[-2] -> second to last
            heads[list_len - n - 1].next = heads[list_len - n + 1]
        heads
        print(heads)

        print(head)
        return head


# COPIED: DO THIS YOURSELF!
# TODO: Figure out better way to test ListNode graph based Leetcode problems

# step 1
#  i,j
# head, 2, 3, 4, 5, n, 7, 8

# step 2
#  i                j
# head, 2, 3, 4, 5, n, 7, 8

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         i,j=head, head
#         # move k to point to
#         # the node n, the node we want to remove
#         for k in range(n):
#             j = j.next
#         if j == None:
#             return head.next

#         # move
#         while j.next != None:
#             i = i.next
#             j = j.next
#         i.next = i.next.next
#         return head


# Test cases
@pytest.mark.parametrize(
    "x, expected",
    [
        (-1, False),
        (0, False),
        (10, True),
        (101, True),
        (101000, True),
    ],
)
def test_solution(x, expected):
    solution = Solution()
    assert solution.removeNthFromEnd(x) == expected
