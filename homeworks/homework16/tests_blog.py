from pathlib import Path
from tempfile import TemporaryDirectory

from blog_app.managers import Blog


# Самостоятельное изучение юнит-тесты.
# Напишите файл tests_blog.py с проверками через простые assert (без сторонних тест-библиотек):
# создайте данные, сохраните в JSON, загрузите и проверьте, что автор поста, категория
# и теги не потерялись. Важно: и категорию (cat), и автора берите из загруженного блога,
# например: cat = next(c for c in loaded.categories if c.title == "Backend"),
# затем assert loaded.posts_by_category(cat)[0].author.name == "Иван Петров".
# Запускайте через uv run python tests_blog.py.


def test_blog_save_load():
    # 1. Создаём блог
    blog = Blog()

    # 2. Добавляем автора, категорию и теги
    author = blog.add_author("Иван Петров")
    category = blog.add_category("Backend")

    python_tag = blog.add_tag("Python")
    django_tag = blog.add_tag("Django")

    # 3. Создаём пост
    post = blog.create_post(
        title="Введение в ООП",
        content="Классы и объекты в Python",
        author=author,
        category=category
    )

    # 4. Добавляем теги к посту
    # assert проверяет, истинно ли условие
    # Если имя автора совпадает, программа продолжает выполнение.
    # Если нет — Python вызывает AssertionError
    assert blog.add_tag_to_post(post, python_tag) is True
    assert blog.add_tag_to_post(post, django_tag) is True

    # Проверяем защиту от дубликатов
    assert blog.add_tag_to_post(post, python_tag) is False
    assert len(python_tag.posts) == 1

    # 5. Сохраняем блог во временный JSON-файл
    # TemporaryDirectory() создаёт временную папку для тестового JSON-файла
    # и автоматически удаляет её после проверки
    with TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "blog_test.json"

        blog.save(str(path))

        # 6. Загружаем блог из JSON
        loaded = Blog.load(str(path))

    # 7. Проверяем, что пост сохранился
    assert len(loaded.posts) == 1
    print("Пост сохранился")

    loaded_post = loaded.posts[0]

    assert loaded_post.title == "Введение в ООП"
    assert loaded_post.content == "Классы и объекты в Python"
    print("Название не потерялось")

    # 8. Проверяем автора
    loaded_author = next(
        a for a in loaded.authors
        if a.name == "Иван Петров"
    )

    assert loaded_post.author is loaded_author
    assert loaded_post.author.name == "Иван Петров"
    print("Связь с автором восстановлена")

    # 9. Проверяем категорию
    cat = next(
        c for c in loaded.categories
        if c.title == "Backend"
    )

    assert loaded_post.category is cat
    print("Связь с категорией восстановлена")

    assert (
        loaded.posts_by_category(cat)[0].author.name
        == "Иван Петров"
    )
    print("Поиск по категории работает")

    # 10. Проверяем теги
    assert set(loaded.tags_of_post(loaded_post)) == {
        "Python", "Django"
    }

    # 11. Проверяем обратную связь тега с постом
    tag = next(
        t for t in loaded.tags
        if t.title == "Python"
    )

    assert loaded.posts_by_tag(tag) == [loaded_post]
    print("Теги сохранились")

    print("Все тесты успешно пройдены!")


if __name__ == "__main__":
    test_blog_save_load()
