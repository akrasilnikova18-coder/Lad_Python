from l15_blog import Comment


def main() -> None:
    comment1 = Comment(author="Игорь", text="Мой первый комментарий", likes=56)
    comment2 = Comment(author="Игорь", text="Мой первый комментарий", likes=56)
    comment3 = Comment(author="Анна", text="Мой второй комментарий", tags=["Python", "Django"])

    print(comment1)
    print(comment1 == comment2) # по значениям
    print(comment1 is comment2) # по ячейке в памяти
        
    comment1.tags.append("JavaScript")
    print(comment1.tags)
    print(comment2.tags)
    print(comment3.tags)


if __name__ == "__main__":
    main()