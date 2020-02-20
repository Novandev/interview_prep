"""
Basic binary tree, Not BST supports most common operations and fills left to right
"""
from queue import Queue


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

    def breadth_first_traversal(self,subtree):
        q = Queue()
        q.put(subtree)
        while not q.empty():
            node = q.get()
            print(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        