import logging

logging.basicConfig(level=logging.INFO)

def find_max_value(root):
    """Знаходить найбільше значення у будь-якому бінарному дереві."""
    if root is None:
        raise ValueError("Дерево порожнє, немає максимального значення")

    max_value = root.val
    if root.left:
        max_value = max(max_value, find_max_value(root.left))
    if root.right:
        max_value = max(max_value, find_max_value(root.right))
    
    return max_value

def find_max_with_logging(root):
    """Функція-обгортка для логування кінцевого результату"""
    if root is None:
        logging.warning("Дерево порожнє! Немає максимального значення.")
        return None

    max_value = find_max_value(root)
    logging.info(f"Найбільше значення у дереві: {max_value}")
    return max_value

def find_min_value(root):
    """Знаходить найменше значення у будь-якому бінарному дереві."""
    if root is None:
        raise ValueError("Дерево порожнє, немає мінімального значення")

    min_value = root.val
    if root.left:
        min_value = min(min_value, find_min_value(root.left))
    if root.right:
        min_value = min(min_value, find_min_value(root.right))
    
    return min_value

def find_min_with_logging(root):
    """Функція-обгортка для логування кінцевого результату"""
    if root is None:
        logging.warning("Дерево порожнє! Немає мінімального значення.")
        return None

    min_value = find_min_value(root)
    logging.info(f"Найменше значення у дереві: {min_value}")
    return min_value

def sum_tree_values(root):
    """
    Функція обчислює суму всіх значень у будь-якому бінарному дереві.
    
    :param root: корінь дерева
    :return: сума значень у дереві або 0, якщо дерево порожнє
    """
    if root is None:
        return 0

    return root.val + sum_tree_values(root.left) + sum_tree_values(root.right)

def sum_tree_with_logging(root):
    """Функція-обгортка для логування кінцевого результату"""
    total_sum = sum_tree_values(root)
    logging.info(f"Сума всіх значень у дереві: {total_sum}")
    return total_sum
