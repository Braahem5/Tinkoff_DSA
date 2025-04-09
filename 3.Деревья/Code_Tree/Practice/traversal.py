class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def iterative_preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value)  # Process the node

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def iterative_inorder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.value)  # Process the node
        current = current.right


def iterative_postorder(root):
    if root is None:
        return

    stack = []
    output = []

    stack.append(root)

    while stack:
        node = stack.pop()
        output.append(node.value)  # Process the node

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    while output:
        print(output.pop())  # Print in reverse order


# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(10)

# Example usage:
# Constructing a simple binary tree
#         5
#        / \
#       3   8
#      / \   \
#     1   4   10


print("Iterative Pre-Order Traversal:")
iterative_preorder(root)

print("\nIterative In-Order Traversal:")
iterative_inorder(root)

print("\nIterative Post-Order Traversal:")
iterative_postorder(root)
