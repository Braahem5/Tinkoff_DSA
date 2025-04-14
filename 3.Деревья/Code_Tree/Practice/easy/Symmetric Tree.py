class TreeNode:
    def __init__(
        self,
        val,
    ):
        self.val = val
        self.left = None
        self.right = None


# A Recursive Approach
class Solution:
    def isSymmetric(self, node: TreeNode):
        if not node:
            return True

        def isMirror(node_T1, node_T2):
            if not node_T1 and not node_T2:
                return True
            if not node_T1 or not node_T2:
                return False

            return (
                node_T1.val == node_T2.val
                and isMirror(node_T1.left, node_T2.right)
                and isMirror(node_T1.right, node_T2.left)
            )

        return isMirror(node.left, node.right)


# Example usage:
# Constructing a symmetric tree
#        1
#      /   \
#     2     2
#    / \   / \
#   3   4 4   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root))  # Output: True

# An Iterative Approach
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    # Initialize a queue for level order traversal
    queue = deque([(root.left, root.right)])

    while queue:
        t1, t2 = queue.popleft()

        # If both nodes are None, continue to the next pair
        if not t1 and not t2:
            continue

        # If one of the nodes is None or their values are not equal, it's not symmetric
        if not t1 or not t2 or t1.val != t2.val:
            return False

        # Enqueue the children in the order that checks for symmetry
        queue.append((t1.left, t2.right))  # Left of t1 with Right of t2
        queue.append((t1.right, t2.left))  # Right of t1 with Left of t2

    return True
