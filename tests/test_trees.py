import pytest
from tree.bst import BST
from tree.avl import AVLTree
from tree.utils import find_max_value, find_min_value, sum_tree_values

# Тестування BST
def test_find_max_bst():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(3)

    assert bst.find_max() == 20

def test_find_min_bst():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(3)

    assert bst.find_min() == 3

def test_sum_bst():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(20)
    bst.insert(3)

    assert bst.sum_values() == 53

# Тестування AVL-дерева
def test_find_max_avl():
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(20)
    avl.insert(3)

    assert avl.find_max() == 20

def test_find_min_avl():
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(20)
    avl.insert(3)

    assert avl.find_min() == 3

def test_sum_avl():
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(20)
    avl.insert(3)

    assert avl.sum_values() == 53

# Тестування загального бінарного дерева
def test_find_max_general_tree():
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    root = TreeNode(10)
    root.left = TreeNode(50)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(100)
    
    assert find_max_value(root) == 100

def test_find_min_general_tree():
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    root = TreeNode(10)
    root.left = TreeNode(50)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(100)

    assert find_min_value(root) == 5

def test_sum_general_tree():
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    root = TreeNode(10)
    root.left = TreeNode(50)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(100)

    assert sum_tree_values(root) == 195
