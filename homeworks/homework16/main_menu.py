from blog_app.managers import Blog
from blog_app.models import Author, Category, Tag, Post


# Интерактивное меню CLI. Превратите main.py в настоящую утилиту с циклом команд:
# add-author, add-category, add-tag, create-post, add-tag-to-post, show, search <категория>,
# save, load, quit. Например, команда create-post запрашивает заголовок, текст, автора и категорию
# по имени. Подсказка: считывайте строку через input(), разбивайте через split(),
# а неизвестную команду — просто сообщайте об этом.


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


def find_tag(blog: Blog, title: str) -> Tag | None:
    for tag in blog.tags:
        if tag.title == title:
            return tag
    return None


def find_post(blog: Blog, title: str) -> Post | None:
    for post in blog.posts:
        if post.title == title:
            return post
    return None


def find_posts(blog: Blog, text: str) -> list[Post]:
    posts = []
    for post in blog.posts:
        if text in post.content or text in post.title:
            posts.append(post)
    return posts


def main() -> None:
    blog = Blog()

    print("""
    ---------------МЕНЮ---------------
    1 - add-author
    2 - add-category
    3 - add-tag
    4 - create-post
    5 - add-tag-to-post
    6 - save
    7 - load
    8 - show
    9 - search <категория>
    10 - quit
    """)

    while True:
        command = input("Введите команду ").lower().strip()

        match command:
            case "1" | "add-author":
                author = input("Введите имя автора ")
                try:
                    blog.add_author(author)
                except ValueError as error:
                    print(f"Ошибка: {error}")
                    
            case "2" | "add-category":
                category = input("Введите название категории ")
                try:
                    blog.add_category(category)
                except ValueError as error:
                    print(f"Ошибка: {error}")
                    
            case "3" | "add-tag":
                tag = input("Введите название тега ")
                try:
                    blog.add_tag(tag)
                except ValueError as error:
                    print(f"Ошибка: {error}")

            case "4" | "create-post":
                title = input("Введите название поста: ")
                content = input("Введите текст поста: ")

                # Выбираем автора
                author_names = ", ".join(
                    author.name for author in blog.authors
                )

                author_name = input(
                    f"Выберите автора ({author_names}): "
                ).strip()

                # Находим объект Author
                author = find_author(blog, author_name)

                if author is None:
                    print("Автор не найден")

                else:
                    # Выбираем категорию
                    category_titles = ", ".join(
                        category.title for category in blog.categories
                    )

                    category_title = input(
                        f"Выберите категорию ({category_titles}): "
                    ).strip()

                    # Находим объект Category
                    category = find_category(blog, category_title)

                    if category is None:
                        print("Категория не найдена")

                    else:
                        # Создаём пост
                        post = blog.create_post(
                            title=title,
                            content=content,
                            author=author,
                            category=category
                        )

                        print(f"Пост «{post.title}» успешно создан!")

            case "5" | "add-tag-to-post":
                # Показываем доступные посты
                print("Доступные посты:")
                for post in blog.posts:
                    print(f"- {post.title}")

                # Пользователь выбирает пост
                post_title = input("Введите название поста: ").strip()
                post = find_post(blog, post_title)

                if post is None:
                    print("Пост не найден")

                else:
                    # Показываем доступные теги
                    print("Доступные теги:")
                    for tag in blog.tags:
                        print(f"- {tag.title}")

                # Пользователь выбирает тег
                tag_title = input("Введите название тега: ").strip()
                tag = find_tag(blog, tag_title)

                if tag is None:
                    print("Тег не найден")
                else:
                    blog.add_tag_to_post(post=post, tag=tag)
                    print(f"Тег «{tag.title}» добавлен к посту «{post.title}»")
                    
            case "6" | "save":
                blog.save("blog.json")
                print("Блог сохранён в blog.json")
                
            case "7" | "load":
                loaded = Blog.load("blog.json")
                
            case "8" | "show":
                print("\nВсе посты:")
                for post in loaded.posts:
                    print(f"  [{post.id}] {post.title} — {post.author.name}, категория: {post.category.title})")
                    print(f"      теги: {', '.join(post.tag_titles) or 'нет'}")
                
            case "9" | "search":
                category_titles = ", ".join(
                    category.title for category in loaded.categories
                )

                name = input(f"Выберите категорию ({category_titles}): ").strip()

                target = find_category(loaded, name)

                if target is not None:
                    print(f"\nПосты категории «{target.title}»:")

                    for post in loaded.posts_by_category(target):
                        print(f"  - {post.title} (автор: {post.author.name})")
                else:
                    print("Категория не найдена")

            case "10" | "quit":
                print("Завершение работы")
                break

            case _:
                print("Неизвестная команда")


if __name__ == "__main__":
    main()