from tree.utils import find_max_with_logging, find_min_with_logging, sum_tree_with_logging

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ Додає новий вузол у дерево """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        """ Рекурсивна допоміжна функція для вставки """
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def find_max(self):
        """ Повертає найбільше значення в дереві """
        return find_max_with_logging(self.root)

    def find_min(self):
        """ Повертає найменше значення в дереві """
        return find_min_with_logging(self.root)

    def sum_values(self):
        """ Обчислює суму всіх значень у дереві """
        return sum_tree_with_logging(self.root)
