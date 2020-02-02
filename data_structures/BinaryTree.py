"""
Basic binary tree, Not BST supports most common operations and fills left to right
"""


class _BinTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def preorder_traversal(self,subtree):
        if subtree is not None:
            print(subtree.data)
            self.preorder_traversal(subtree.left)
            self.preorder_traversal(subtree.right)

    def inorder_traversal(self,subtree):
        if subtree is not None:
            self.preorder_traversal(subtree.left)
            print(subtree.data)
            self.preorder_traversal(subtree.right)

    def postorder_traversal(self,subtree):
        if subtree is not None:
            self.preorder_traversal(subtree.left)
            self.preorder_traversal(subtree.right)
            print(subtree.data)
