# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum_recursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        node = targetSum - root.val

        if not root.left and not root.right:
            return node == 0

        return self.hasPathSum_recursive(root.left, node) or self.hasPathSum_recursive(
            root.right, node
        )

    def hasPathSum_iterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            currnent_node, remaining_sum = stack.pop()

            if not currnent_node.left and not currnent_node.right:
                if remaining_sum == 0:
                    return True

            if currnent_node.left:
                stack.append(
                    (currnent_node.left, remaining_sum - currnent_node.left.val)
                )
            if currnent_node.right:
                stack.append(
                    (currnent_node.right, remaining_sum - currnent_node.right.val)
                )
        return False
