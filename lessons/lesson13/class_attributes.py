class Post:
    platform = "Blog CLI"

    def __init__(self, title: str, author: str, text: str) -> None:
        self.title = title
        self.author = author
        self.text = text
        self.likes = 0

    def display(self) -> None:
        print(f"Название статьи: {self.title}, Автор: {self.author}, Количество лайков: {self.likes}")

    def add_like(self) -> None:
        self.likes += 1


first = Post(title="Занимательная физика", author="Алла", text="Мой первый пост. Мой второй пост.")
second = Post(title="Занимательная математика", author="Игорь", text="Мой третий пост. Мой четвертый пост.")

first.add_like()
first.add_like()
second.add_like()

first.display()
second.display()

print(first.platform)
print(second.platform)
print(Post.platform)

Post.display(first)
