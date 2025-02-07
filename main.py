from tree.bst import BST
from tree.avl import AVLTree
from tree.utils import find_max_with_logging, find_min_with_logging, sum_tree_with_logging
from comments.comment_system import Comment, save_comments, load_comments

def main_menu():
    bst = BST()
    avl = AVLTree()
    comments = load_comments()  # Автоматичне завантаження коментарів з файлу

    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Додати елементи в BST")
        print("2. Додати елементи в AVL")
        print("3. Знайти найбільше значення у BST")
        print("4. Знайти найменше значення у BST")
        print("5. Знайти найбільше значення у AVL")
        print("6. Знайти найменше значення у AVL")
        print("7. Обчислити суму всіх значень у BST")
        print("8. Обчислити суму всіх значень у AVL")
        print("9. Робота з коментарями")
        print("10. Вийти")

        choice = input("Виберіть опцію (1-10): ")

        if choice == "1":
            elements = input("Введіть числа через пробіл: ").strip()
            for num in elements.split():
                if num.isdigit():
                    bst.insert(int(num))
            print("Елементи додані у BST.")

        elif choice == "2":
            elements = input("Введіть числа через пробіл: ").strip()
            for num in elements.split():
                if num.isdigit():
                    avl.insert(int(num))
            print("Елементи додані у AVL.")

        elif choice == "3":
            max_value = bst.find_max()
            if max_value is not None:
                print("Найбільше значення у BST:", max_value)
            else:
                print("Дерево порожнє, немає максимального значення.")

        elif choice == "4":
            min_value = bst.find_min()
            if min_value is not None:
                print("Найменше значення у BST:", min_value)
            else:
                print("Дерево порожнє, немає мінімального значення.")

        elif choice == "5":
            max_value = avl.find_max()
            if max_value is not None:
                print("Найбільше значення у AVL:", max_value)
            else:
                print("Дерево порожнє, немає максимального значення.")

        elif choice == "6":
            min_value = avl.find_min()
            if min_value is not None:
                print("Найменше значення у AVL:", min_value)
            else:
                print("Дерево порожнє, немає мінімального значення.")

        elif choice == "7":
            total_sum = bst.sum_values()
            print("Сума всіх значень у BST:", total_sum)

        elif choice == "8":
            total_sum = avl.sum_values()
            print("Сума всіх значень у AVL:", total_sum)

        elif choice == "9":
            comment_menu(comments)

        elif choice == "10":
            print("Вихід...")
            save_comments(comments)  # Збереження перед виходом
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")

def comment_menu(comments):
    """Меню для взаємодії з коментарями"""
    while True:
        print("\n=== МЕНЮ КОМЕНТАРІВ ===")
        print("1. Додати кореневий коментар")
        print("2. Відповісти на коментар")
        print("3. Видалити коментар")
        print("4. Відобразити всі коментарі")
        print("5. Повернутися до головного меню")

        choice = input("Виберіть опцію (1-5): ")

        if choice == "1":
            text = input("Введіть текст коментаря: ")
            author = input("Автор коментаря: ")
            comments.append(Comment(text, author))
            save_comments(comments)  # Збереження у файл
            print("Коментар додано.")

        elif choice == "2":
            if not comments:
                print("Немає коментарів для відповіді.")
                continue

            comment = select_comment(comments)  # Вибір будь-якого коментаря
            if comment:
                reply_to_comment(comment, comments)  # Додаємо відповідь

        elif choice == "3":
            if not comments:
                print("Немає коментарів для видалення.")
                continue

            comment = select_comment(comments)  # Вибираємо будь-який коментар
            if comment:
                comment.remove_reply()
                save_comments(comments)  # Збереження змін
                print("Коментар видалено.")

        elif choice == "4":
            if comments:
                print("\n=== ВІДОБРАЖЕННЯ КОМЕНТАРІВ ===")
                for comment in comments:
                    comment.display()
            else:
                print("Немає коментарів.")

        elif choice == "5":
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")

def select_comment(comments):
    """Дозволяє користувачеві вибрати вкладений коментар"""
    print("\n=== СПИСОК КОМЕНТАРІВ ===")
    comment_list = []
    enumerate_comments(comments, comment_list, level=0)  # Заповнюємо список

    if not comment_list:
        print("Немає доступних коментарів.")
        return None

    for i, (comment, _) in enumerate(comment_list, start=1):
        print(f"{i}. {comment.author}: {comment.text}")

    try:
        index = int(input("Виберіть номер коментаря: ")) - 1
        if 0 <= index < len(comment_list):
            return comment_list[index][0]
        else:
            print("Неправильний вибір.")
            return None
    except ValueError:
        print("Помилка: потрібно ввести число!")
        return None

def enumerate_comments(comments, comment_list, level=0):
    """Рекурсивно збирає всі коментарі та їх вкладені відповіді"""
    for comment in comments:
        comment_list.append((comment, level))
        enumerate_comments(comment.replies, comment_list, level + 1)

def reply_to_comment(comment, comments):
    """Рекурсивно дозволяє відповідати на коментар або відповідь"""
    while True:
        print("\n=== Коментар ===")
        comment.display()
        print("\n1. Відповісти на цей коментар")
        print("2. Вийти")

        choice = input("Виберіть опцію (1-2): ")

        if choice == "1":
            text = input("Введіть текст відповіді: ")
            author = input("Автор відповіді: ")
            new_reply = Comment(text, author)
            comment.add_reply(new_reply)
            save_comments(comments)  # Тепер передаємо `comments`
            print("Відповідь додана.")
        elif choice == "2":
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
