class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height of the node


class AVLTree:
    def insert(self, root, data):
        # Step 1: Perform the normal BST insertion
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Step 2: Update the height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor
        balance = self.get_balance(root)

        # Step 4: If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (unchanged) node pointer
        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.data), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def isValid(self, root):

        def valid(node, left, right):
            if node is None:
                return True

            if not (left < node.data and node.data < right):
                return False
            return valid(node.left, left, node.data) and valid(
                node.right, node.data, right
            )

        return valid(root, float("-inf"), float("inf"))


# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    # Insert nodes
    data = [10, 20, 30, 40, 50, 25]
    for value in data:
        root = avl_tree.insert(root, value)

    # Pre-order traversal of the AVL tree
    print("Pre-order traversal of the AVL tree is:")
    avl_tree.pre_order(root)
    print()
    print(avl_tree.isValid(root))
