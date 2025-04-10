class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value):
        self.root = TreeNode(value)
        self.length = 1

    # i am trying to implement an iterative pre-order travesal of a tree

    def pre_order(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            current_element = stack.pop()
            result.append(current_element.value)
            if current_element.right:
                stack.append(current_element.right)
            if current_element.left:
                stack.append(current_element.left)

        return result

    def in_order(self, root):
        if root is None:
            return []

        stack = []
        result = []
        current_element = root

        while stack or current_element:
            while current_element:
                stack.append(current_element)
                current_element = current_element.left
            current_element = stack.pop()
            result.append(current_element.value)
            current_element = current_element.right
        return result

    def post_order(self, root):
        if root is None:
            return []

        firstStack = [root]
        secondStack = []
        while firstStack:
            current_element = firstStack.pop()
            secondStack.append(current_element)
            if current_element.left:
                firstStack.append(current_element.left)
            if current_element.right:
                firstStack.append(current_element.right)

        result = []
        while secondStack:
            result.append(secondStack.pop().value)

        return result
