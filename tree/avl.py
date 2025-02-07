class AVLNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1  # Висота вузла

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ Вставка нового вузла в AVL-дерево """
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """ Рекурсивна вставка з балансуванням """
        if node is None:
            return AVLNode(key)

        if key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _balance(self, node):
        """ Балансування вузла """
        balance = self._get_balance(node)

        # Лівий-лівий випадок
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Правий-правий випадок
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Лівий-правий випадок
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Правий-лівий випадок
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def find_max(self):
        """ Знаходить найбільше значення в AVL-дереві """
        from tree.utils import find_max_with_logging
        return find_max_with_logging(self.root)

    def find_min(self):
        """ Знаходить найменше значення в AVL-дереві """
        from tree.utils import find_min_with_logging
        return find_min_with_logging(self.root)

    def sum_values(self):
        """ Обчислює суму всіх значень у AVL-дереві """
        from tree.utils import sum_tree_with_logging
        return sum_tree_with_logging(self.root)
