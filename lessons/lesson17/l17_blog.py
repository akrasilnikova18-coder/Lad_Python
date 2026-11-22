import json
import keyword
from dataclasses import dataclass
from json import JSONDecodeError
from pathlib import Path


DB_PATH = Path("blog.json")


@dataclass
class Post:
    title: str
    author: str
    category: str
    views: int=0

    def as_dict(self) -> dict[str, object]:
        return {"title": self.title, "author": self.author, "category": self.category, "views": self.views}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Post":
        return cls(title=str(data["title"]), author=str(data["author"]), category=str(data["category"]), views=int(data["views"]))

    def __str__(self) -> str:
        return f"Название: {self.title}, Автор: {self.author}, Категория: {self.category}, Просмотры: {self.views}"


class BlogRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def load(self) -> list["Post"]:
        if not self.db_path.exists():
            return []
        try:
            with open(self.db_path, "r", encoding="utf-8") as file:
                raw = json.load(file)
        except JSONDecodeError as error:
            raise ValueError("Некорректный файл, файл поврежден") from error
        return [Post.from_dict(post) for post in raw]

    def save(self, posts: list["Post"]) -> None:
        data = [post.as_dict() for post in posts]

        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def add_posts(posts: list["Post"]) -> None:
    title = input("Введите название ")
    author = input("Введите автора ")
    category = input("Введите категорию ")

    if not title or not author or not category:
        raise ValueError("Все поля обязательны")

    posts.append(Post(title=title, author=author, category=category))
    print("Пост добавлен")


def list_posts(posts: list["Post"]) -> None:
    if not posts:
        print("Нет постов")
        return
    else:
        for num, post in enumerate(posts, start=1):
            print(f"{num}. {post}")


def search_posts(posts: list["Post"], keyword: str) -> list["Post"]:
    keyword = keyword.lower().strip()
    return [post for post in posts if post.title.lower() == keyword]


def main() -> None:
    repo = BlogRepository(DB_PATH)

    try:
        posts = repo.load()
    except ValueError as error:
        print(f"Ошибка при загрузке: {error}")
        posts = []

    print("""
    Меню:
    1 - add
    2 - list
    3 - find
    4 - exit
    """)

    while True:
        command = input("Введите команду ").strip().lower()

        match command:
            case "add" | "1":
                try:
                    add_posts(posts)
                except ValueError as error:
                    print(f"Ошибка заполнения: {error}")
            case "list" | "2":
                list_posts(posts)
            case "find" | "3":
                keyword = input("Введите ключевое слово: ")
                if search_result := search_posts(posts, keyword):
                    list_posts(search_result)
                else:
                    print("Ничего не найдено")
            case "exit" | "1":
                try:
                    repo.save(posts)
                    print("Все сохранено")
                    break
                except OSError:
                    print("Не удалось сохранить файл")
                    break
            case _:
                print("Неизвестная команда")

if __name__ == '__main__':
    main()
