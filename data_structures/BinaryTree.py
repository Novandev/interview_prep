"""
Basic binary tree, Not BST supports most common operations and fills left to right
"""


class _BinTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
