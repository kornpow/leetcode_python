
import pytest
from typing import List, Optional, Type

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list_to_linkedlist(cls, values):
        if len(values) == 0:
            return None

        head = cls(values[0])
        current = head
        for val in values[1:]:
            current.next = cls(val)
            current = current.next

        return head

    def __repr__(self):
        result = []
        current = self
        while current is not None:
            result.append(str(current.val))
            current = current.next
        return "->".join(result)
    
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        
        current_self = self
        current_other = other
        
        while current_self is not None and current_other is not None:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        
        return current_self is None and current_other is None

# Paste the LeetCode solution class here
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        # create empty linked list
        head = ListNode(None)
        current1 = list1
        current2 = list2
        
        # keep going until we've iterated through both LL
        while current1 or current2:

            cval1 = float("inf") if not current1 else current1.val
            cval2 = float("inf") if not current2 else current2.val

            if cval1 < cval2:
                head.val = current1.val
                current1 = current1.next
            else:
                head.val = current2.val
                current2 = current2.next

            head.next = ListNode(None)
            head = head.next

        return head

        # print(list1)
        # print(list2)

        # return ListNode(1)

# Test cases
@pytest.mark.parametrize("list1, list2, expected", [
    # ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    # ([], [], []),
    ([],[0], [0]),
    # ([1,1,1,1,1],[1,1], [1,1,1,1,1,1,1]),

])
def test_solution(list1, list2, expected):
    solution = Solution()
    expected =  ListNode.list_to_linkedlist(expected)
    nodeList1 = ListNode.list_to_linkedlist(list1)
    nodeList2 = ListNode.list_to_linkedlist(list2)

    # assert 1 == 0
    assert solution.mergeTwoLists(nodeList1, nodeList2) == expected
