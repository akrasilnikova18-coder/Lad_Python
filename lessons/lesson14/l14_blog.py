from abc import ABC, abstractmethod
from typing import override


class Content(ABC):
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "04/11/2026"

    @abstractmethod
    def get_summary(self) -> str:
        """Возвращает информацию о контенте"""
        return f"Контент - {self.title} создан {self.created_at}"


class Post(Content):
    def __init__(self, title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    @override
    def get_summary(self) -> str:
        return f"Пост создан - {self.created_at} автором {self.author}"


class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    @override
    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base} - {self.slug}"


def print_items(items: list[Content]) -> None:
    for item in items:
        print(item.get_summary())


def main() -> None:
    items = []

    print("Меню: 1 - add_post, 2 - add_page, 3 - list, 4 - exit")

    while True:
        to_do = input("Введите команду ").strip()

        if to_do in ["1", "add_post"]:
            title = input("Введите название поста ")
            body = input("Введите текст поста ")
            author = input("Введите автора ")
            items.append(Post(title=title, body=body, author=author))
            
        elif to_do in ["2", "add_page"]:
            title = input("Введите название страницы ")
            slug = input("Введите слаг ")
            items.append(Page(title=title, slug=slug))
            
        elif to_do in ["3", "list"]:
            print_items(items)

        elif to_do in ["4", "exit"]:
            print("Завершение работы")
            break

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()