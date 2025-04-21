from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class solution:
    def arrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.arrayToBST(nums[:mid])
        root.right = self.arrayToBST(nums[mid + 1 :])
        return root

    # iterative
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Create a stack to hold the tuples of (start, end) indices
        stack = [(0, len(nums) - 1)]
        root = None

        while stack:
            start, end = stack.pop()
            if start > end:
                continue

            mid = (start + end) // 2
            node = TreeNode(nums[mid])

            if root is None:
                root = node

            # Push right child first so that left child is processed first
            stack.append((mid + 1, end))  # Right subtree
            stack.append((start, mid - 1))  # Left subtree

            # Attach the node to the correct parent
            if stack:
                parent_start, parent_end = stack[-1]
                parent_mid = (parent_start + parent_end) // 2
                if nums[mid] < nums[parent_mid]:
                    # Attach to the left of the parent
                    if not stack[-1][0] == mid + 1:  # Ensure it's not the right child
                        stack[-1] = (
                            parent_start,
                            parent_mid - 1,
                        )  # Update the parent range
                        stack.append((start, mid - 1))  # Left child
                else:
                    # Attach to the right of the parent
                    if not stack[-1][1] == mid - 1:  # Ensure it's not the left child
                        stack[-1] = (
                            parent_mid + 1,
                            parent_end,
                        )  # Update the parent range
                        stack.append((mid + 1, end))  # Right child

        return root
