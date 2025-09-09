
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

    # def __repr__(self):
    #     return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

    def __repr__(self):
        return f"TreeNode(val={self.val})"

# Paste the LeetCode solution class here
class Solution:
    solution = []

    # Time Complexity:
    # Space Complexity: 
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        print(root)
        
        # Stack stores: [node, path_to_that_node]
        stack = [ [root, [str(root.val)]], ]  # Each entry is [current_node, path_so_far]

        while stack:
            node, path = stack.pop()
            print(f"NODE: {node.val}... PATH: {path}")

            if not node.left and not node.right:
                results.append("->".join(path))
                print(f"FOUND LEAF PATH: {path}")

            if node.left:
                print("GO LEFT!")
                new_path = path + [str(node.left.val)]
                stack.append([node.left, new_path])

            if node.right:
                print("GO RIGHT!")
                new_path = path + [str(node.right.val)]
                stack.append([node.right, new_path])

            print(stack)
        
        print(results)
        return results


    def dfs(self, node: TreeNode, all_paths: List[List[int]], current_path: List[int]):

        if not node:
            print("WE SHOULDN'T BE HERE")
            return
        
        current_path.append(str(node.val))
        # found a leaf
        if not node.left and not node.right:
            print("FOUND A LEAF!")
            print(current_path)
            all_paths.append("->".join(current_path))

        if node.left:
            self.dfs(node.left, all_paths, current_path)

        if node.right:
            self.dfs(node.right, all_paths, current_path)

        current_path.pop()

    

    # Time Complexity:
    # Space Complexity:     
    def binaryTreePathRecursion(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []

        all_paths = []
        current_path = []

        # all_paths in shared memory and paths are added when found
        self.dfs(root, all_paths, current_path)
        
        print("All solutions:")
        print(all_paths)
        return all_paths


# Test cases
@pytest.mark.parametrize("node_list, expected_path_list", [
    ([1,2,3,None,5], ["1->2->5","1->3"]),
    ([1], ["1"]),
])
def test_solution(node_list, expected_path_list):
    root = TreeNode.from_list(node_list)
    solution = Solution()
    assert set(solution.binaryTreePaths(root)) == set(expected_path_list)

    assert set(solution.binaryTreePathRecursion(root)) == set(expected_path_list)


def monkey():
    import code
    a = TreeNode.from_list([1,2,3,None,5])
    code.interact(local=dict(globals(), **locals()))
    # solution = Solution()
    # assert solution.binaryTreePaths(None) == []


if __name__ == "__main__":
    monkey()