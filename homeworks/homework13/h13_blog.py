# Мини-проект «Блог CLI» — причесать. Взять классы Post/Author/Category из Этапа 4 и добавить:
# (а) статический метод Post.is_valid_text(text) (текст не пустой),
# (б) метод класса Author.from_csv(line) (разбирает строку имя;email),
# (в) возможность вывести только посты одной категории.


class Author:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        
    @classmethod
    def from_csv(cls, row: str) -> "Author":
        name, email = row.split(";")
        return Author(name, email)


class Category:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


class Post:
    def __init__(
        self, title: str, text: str, author: Author, category: Category
    ) -> None:
        self.title = title
        self.text = text
        self.author = author
        self.category = category

    def display(self):
        print(
            f"Категория: {self.category}, Название: {self.title}, Автор: {self.author.name}"
        )
        
    @staticmethod
    def is_valid_text(text: str) -> bool:
        return isinstance(text, str) and bool(text.strip())
    
    def find_for_category(self, category: str) -> None:
        for post in posts:
            if post.category.title == category:
                self.display()
            else:
                print(f"Постов в категории {category} не найдено.")

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
    print(f"Текст поста пустой? {new_post.is_valid_text(text)}")


def show_posts() -> None:
    if not posts:
        print("Нет записей")
        return

    for post in posts:
        post.display()
        
        
def find_posts() -> None:
    category_finded = input("Введите название категории ")
    for post in posts:
        post.find_for_category(category_finded)


while True:
    action = input("Выберите действие: add, show, find или exit ").strip().lower()

    if action == "add":
        add_post()
    elif action == "show":
        show_posts()
    elif action == "find":
        find_posts()
    elif action == "exit":
        print("Завершение работы")
        break
    else:
        print("Непонятная команда")
