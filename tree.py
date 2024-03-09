class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def display(self):
        self._display_recursively(self.root)

    def _display_recursively(self, node):
        if node:
            self._display_recursively(node.left)
            print(node.data)
            self._display_recursively(node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    print("Tree Structure:")
    tree.display()
