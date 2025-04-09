class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.length += 1
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return "Empty Tree"

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                self.length += 1
            else:
                return self._insert_recursive(node.left, value)
        else:  # handle multiple equal values
            if node.right is None:
                node.right = Node(value)
                self.length += 1
            else:
                return self._insert_recursive(node.right, value)

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

    def get_length(self):
        return self.length

    def level_order_traversal(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        if node is None:
            return False

        if target == node.value:
            return True
        elif target < node.value:
            return self._search_recursive(node.left, target)
        else:
            return self._search_recursive(node.right, target)

    def delete(self, target):
        deleted = False
        self.root, deleted = self._delete_recursive(self.root, target)
        if deleted:
            self.length -= 1

    def _delete_recursive(self, node, target):
        if node is None:
            return node, False

        if target < node.value:
            node.left, deleted = self._delete_recursive(node.left, target)
            return node, deleted
        elif target > node.value:
            node.right, deleted = self._delete_recursive(node.right, target)
            return node, deleted
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                min_right_sub_tree = self.get_min(node.right)
                node.value = min_right_sub_tree
                node.right, _ = self._delete_recursive(node.right, min_right_sub_tree)
                return (
                    node,
                    True,
                )  # why don't we return the '_' since the function will return two values

    def get_min(self, node):
        if node is None:
            return None
        currentNode = node
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
