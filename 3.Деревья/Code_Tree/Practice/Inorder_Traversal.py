class Solution:
    def inorder_traversal_recursive(self, root):
        if not root:
            return []
        result = []
        result.extend(self.inorder_traversal_recursive(root.left))
        result.append(root.val)
        result.extend(self.inorder_traversal_recursive(root.right))
        return result

    def inorder_traversal_iterative(self, root):
        stack = []
        current_element = root
        result = []

        while stack or current_element:
            while current_element:
                stack.append(current_element)
                current_element = current_element.left
            current_element = stack.pop()
            result.append(current_element.val)
            current_element = current_element.right
        return result
