
import pytest

from typing import List, Optional, Type

# ---- Description ----
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, node_list: List[Optional[int]]) -> Optional['TreeNode']:
        if not node_list or node_list[0] is None:
            return None
        
        # make a tree node from the first element
        root = cls(node_list[0])
        queue = [root]
        index = 1
        while index < len(node_list):
            node = queue.pop(0)
            if index < len(node_list):
                if node_list[index] is not None:
                    node.left = cls(node_list[index])
                    queue.append(node.left)
                index += 1
            if index < len(node_list):
                if node_list[index] is not None:
                    node.right = cls(node_list[index])
                    queue.append(node.right)
                index += 1
        return root

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

# Paste the LeetCode solution class here
class Solution:
    def outputStringWriter(self, path_nodes):
        print("string writer")
        alist = [node for node in path_nodes]
        print(alist)
        result = "->".join(str(val) for val in alist)
        print(result)
        return result

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        print(root)
        
        # Stack stores: [node, path_to_that_node]
        stack = [ [root, [root.val]], ]  # Each entry is [current_node, path_so_far]

        while stack:
            node, path = stack.pop()
            print(f"NODE: {node.val}... PATH: {path}")

            if not node.left and not node.right:
                results.append(path)
                print(f"FOUND LEAF PATH: {path}")

            if node.left:
                print("GO LEFT!")
                new_path = path + [node.left.val]
                stack.append([node.left, new_path])

            if node.right:
                print("GO RIGHT!")
                new_path = path + [node.right.val]
                stack.append([node.right, new_path])

            print(stack)
        
        final_result = [self.outputStringWriter(s) for s in results]
        print(final_result)
        return final_result
        

# Test cases
@pytest.mark.parametrize("node_list, expected_path_list", [
    ([1,2,3,None,5], ["1->2->5","1->3"]),
    ([1], ["1"]),
])
def test_solution(node_list, expected_path_list):
    root = TreeNode.from_list(node_list)
    solution = Solution()
    assert set(solution.binaryTreePaths(root)) == set(expected_path_list)


def monkey():
    import code
    a = TreeNode.from_list([1,2,3,None,5])
    code.interact(local=dict(globals(), **locals()))
    # solution = Solution()
    # assert solution.binaryTreePaths(None) == []


if __name__ == "__main__":
    monkey()