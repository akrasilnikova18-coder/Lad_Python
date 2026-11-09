from h15_blog import Comment


def main() -> None:
    comment1 = Comment(author="Максим", text="Мой первый комментарий", likes=150)
    comment2 = Comment(author="Максим", text="Мой первый комментарий", likes=98)
    comment4 = Comment(author="Максим", text="Мой первый комментарий", likes=98)

    print(comment4==comment2)

    try:
        comment3 = Comment(author="Алла", text="")
        print(comment3)
    except ValueError as e:
        print(e)
        
    comment1.tags.append("python")
    comment1.tags.append("django")

    print(comment1)
    print(comment2)


if __name__ == "__main__":
    main()