from l15_blog import Post, Author


def main() -> None:
    author = Author(name="Анна", email="1233")
    post1 = Post(title="Занимательная физика", author=author, content="Мой первый пост")
    post2 = Post(title="Занимательная математика", author=author, content="Мой второй пост")

    print("Это __str__")
    print(post1)
    print(author)

    print("Это __repr__")
    print(repr(post2))
    print(repr(author))

    print(f"{author} - {author=}") # в первом случае str, во втором - repr

    print("Список постов:") # срабатывает repr, потому что список
    posts = [post1, post2]
    print(posts)


if __name__ == "__main__":
    main()
