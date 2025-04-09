class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.length += 1
            return "inserted root node"
        else:
            self.__insert_recursive(self.root, value)

    def __insert_recursive(self, node, value):
        if not node:
            return "Unable to insert"

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                self.length += 1
                return f"Inserted {value} to the left of {node.value}"
            else:
                return self.__insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                self.length += 1
                return f"Inserted {value} to the right of {node.value}"
            else:
                return self.__insert_recursive(node.right, value)

    def height(self, node):
        if node is None:
            return -1

        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)

    def traversal(self):
        result = []
        return self.__in_order_traversal(self.root, result)

    def __in_order_traversal(self, node, result):
        if node:
            self.__in_order_traversal(node.left, result)
            result.append(node.value)
            self.__in_order_traversal(node.right, result)

        return result

    def Diameter(self, root):
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        left_diameter = self.Diameter(root.left)
        right_diameter = self.Diameter(root.right)

        final_diameter = max(
            left_height + right_height + 2, max(left_diameter, right_diameter)
        )
        return final_diameter


bst = BST()
print(bst.insert(10))
print(bst.insert(5))
print(bst.insert(15))
# print(bst.insert(10))

print("Height of BST:", bst.height(bst.root))  # Get height
print("In-order Traversal:", bst.traversal())  # Get in-order traversal
print("Total Nodes:", bst.length)  # Get total number of nodes
print("Diameter: ", bst.Diameter(bst.root))
