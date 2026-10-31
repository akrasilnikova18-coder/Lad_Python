class Author:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        
        
class Category:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title
        

class Post:
    def __init__(self, title: str, text: str, author: Author, category: Category) -> None:
        self.title = title
        self.text = text
        self.author = author
        self.category = category
        
    def display(self):
        print(f"Категория: {self.category}, Название: {self.title}, Автор: {self.author.name}")
        
        
posts = []

def add_post() -> None:
    author_name = input("Введите имя автора ")
    author_email = input("Введите email автора ")
    category = input("Введите категорию ")
    title = input("Введите название ")
    text = input("Введите текст ")

    new_author = Author(author_name, author_email)
    new_category = Category(category)
    new_post = Post(title, text, new_author, new_category)

    posts.append(new_post)
    print("Пост добавлен\n")


def show_posts() -> None:
    if not posts:
        print("Нет записей")
        return

    for post in posts:
        post.display()


while True:
    action = input("Выберите действие: add, show или exit ").strip().lower()

    if action == "add":
        add_post()
    elif action == "show":
        show_posts()
    elif action == "exit":
        print("Завершение работы")
        break
    else:
        print("Непонятная команда")

