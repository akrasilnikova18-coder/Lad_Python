from blog_app.managers import Blog
from blog_app.models import Author, Category, Tag, Post


def find_category(blog: Blog, title: str) -> Category | None:
    for category in blog.categories:
        if category.title == title:
            return category
    return None


def find_author(blog: Blog, name: str) -> Author | None:
    for author in blog.authors:
        if author.name == name:
            return author
    return None


def main() -> None:
    blog = Blog()

    # 1. создаём авторов, категории и теги
    ivan = blog.add_author("Иван Петров")
    anna = blog.add_author("Анна Смирнова")
    backend = blog.add_category("Backend")
    frontend = blog.add_category("Frontend")
    python_tag = blog.add_tag("Python")
    django_tag = blog.add_tag("Django")
    sql_tag = blog.add_tag("SQL")

    # 2. создаём посты (связываем с автором и категорией)
    post1 = blog.create_post(
        "Введение в ООП",
        "Классы и объекты — основа ООП.",
        author=ivan,
        category=backend,
    )
    post2 = blog.create_post(
        "Django-модели: мост к базе данных",
        "Модели описывают структуру данных и связи таблиц.",
        author=ivan,
        category=backend,
    )
    post3 = blog.create_post(
        "Семантика HTML",
        "Правильная разметка делает страницы доступными.",
        author=anna,
        category=frontend,
    )

    # 3. навешиваем теги (многие-ко-многим)
    blog.add_tag_to_post(post1, python_tag)
    blog.add_tag_to_post(post1, django_tag)
    blog.add_tag_to_post(post2, python_tag)
    blog.add_tag_to_post(post2, django_tag)
    blog.add_tag_to_post(post2, sql_tag)
    blog.add_tag_to_post(post3, python_tag)

    # 4. сохраняем в JSON
    blog.save("blog.json")
    print("Блог сохранён в blog.json")

    # 5. загружаем обратно — как будто стартовала новая сессия
    loaded = Blog.load("blog.json")

    # 6. выводим все посты
    print("\nВсе посты:")
    for post in loaded.posts:
        print(
            f"  [{post.id}] {post.title} — {post.author.name} "
            f"(категория: {post.category.title})"
        )
        print(f"      теги: {', '.join(post.tag_titles) or 'нет'}")

    # 7. поиск по категории (категорию берём из загруженного блога!)
    target = find_category(loaded, "Backend")
    if target is not None:
        print(f"\nПосты категории «{target.title}»:")
        for post in loaded.posts_by_category(target):
            print(f"  - {post.title} (автор: {post.author.name})")

    # 8. посты конкретного автора
    author = find_author(loaded, "Иван Петров")
    if author is not None:
        print(f"\nПосты автора «{author.name}»:")
        for post in loaded.posts_by_author(author):
            print(f"  - {post.title}")


if __name__ == "__main__":
    main()
