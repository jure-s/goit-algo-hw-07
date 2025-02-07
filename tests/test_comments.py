import pytest
from comments.comment_system import Comment

def test_add_reply():
    comment = Comment("Гарна книга!", "Олег")
    reply = Comment("Не погоджуюся!", "Марина")
    comment.add_reply(reply)

    assert len(comment.replies) == 1
    assert comment.replies[0].text == "Не погоджуюся!"

def test_remove_comment():
    comment = Comment("Це тестовий коментар", "Іван")
    comment.remove_reply()

    assert comment.text == "Цей коментар було видалено."
    assert comment.is_deleted

def test_nested_replies():
    comment = Comment("Оригінальний коментар", "Настя")
    reply1 = Comment("Перша відповідь", "Василь")
    reply2 = Comment("Друга відповідь", "Юлія")

    comment.add_reply(reply1)
    reply1.add_reply(reply2)

    assert len(comment.replies) == 1
    assert len(reply1.replies) == 1
    assert reply1.replies[0].text == "Друга відповідь"
