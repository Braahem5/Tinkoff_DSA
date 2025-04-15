from collections import deque


class TreeNode:
    def __init__(
        self,
        val,
    ):
        self.val = val
        self.left = None
        self.right = None


# A Recursive Approach
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# An Itertive Approach
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        Que = deque([(p, q)])
        while Que:
            node1, node2 = Que.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            Que.append([(node1.left, node2.left)])
            Que.append([(node1.right, node2.right)])

        return True
