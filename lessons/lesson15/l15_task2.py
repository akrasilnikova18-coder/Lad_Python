from l15_blog import Post, Author


def main() -> None:
    author = Author(name="Анна", email="1233")
    post1 = Post(title="Занимательная физика", author=author, content="Мой первый пост")
    
    print("Это @property")
    print(post1.title)
    print(post1.title_length)
    print(post1.slug)
    
    post1.title = "Занимательная алгебра"
    print(post1.title)

    try:
        post1.title = "     "
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()