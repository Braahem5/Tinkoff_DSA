class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)
        self.length = 1

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                self.length += 1
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                self.length += 1
            else:
                self._insert_recursive(node.right, value)

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        if node is None:
            return False
        elif node.value == target:
            return True
        elif target < node.value:
            return self._search_recursive(node.left, target)
        else:
            return self._search_recursive(node.right, target)

    def delete(self, target):
        self.root = self._delete_recursion(self.root, target)

    def _delete_recursion(self, node, target):
        if node is None:
            return node

        if target < node.value:
            node.left = self._delete_recursion(node.left, target)
        elif target > node.value:
            node.right = self._delete_recursion(node.right, target)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._min_value_node(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursion(node.right, min_larger_node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __str__(self):
        return self._preorder_traversal(self.root).strip()

    def _preorder_traversal(self, node):
        if node is None:
            return ""
        return (
            str(node.value)
            + " "
            + self._preorder_traversal(node.left)
            + self._preorder_traversal(node.right)
        )


# Example usage
tree = Tree(15)
tree.insert(10)
tree.insert(20)
tree.insert(8)
tree.insert(12)

print("Preorder Traversal of the BST:", tree)
print("Search for 10:", tree.search(10))
print("Search for 25:", tree.search(25))  # Fixed the search value to 25
print("Search for 8:", tree.search(8))  # Added search for 8

# Deleting a node
tree.delete(10)
print("Preorder Traversal after deleting 10:", tree)
