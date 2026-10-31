from typing import Self


class Post:
    def __init__(self, title: str, author: str, text: str) -> None:
        self.title = title
        self.author = author
        self.text = text
        self.likes = 0

    def display(self) -> None:
        print(f"Название статьи: {self.title}, Автор: {self.author}")

    @staticmethod
    def is_valid_title(title: str) -> bool:
        return isinstance(title, str) and bool(title.strip())

    @classmethod
    def from_csv(cls, row: str) -> Self: # вариант "Post"
        title, author, text = row.split(";")
        if not cls.is_valid_title(title): # False превращаем в True, чтобы сработал if
            raise ValueError("Пустой заголовок недопустим")
        return cls(title, author, text)


post = Post.from_csv("Занимательная физика;Алла;Мой первый пост. Мой второй пост.")
post.display()

print(Post.is_valid_title("Занимательная математика"))
print(Post.is_valid_title(1))
print(post.is_valid_title(post.title))


title = input("Введите заголовок статьи ")
author = "Артем"
text = "Мой третий пост"

if Post.is_valid_title(title):
    new_post = Post(title, author, text)
    new_post.display()
else:
    print("Некорректный заголовок")
