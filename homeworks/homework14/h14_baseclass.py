from abc import abstractmethod
from typing import override


# Базовый класс + два наследника на данных блога. Создайте абстрактный класс Content с полями
# title и created_at и абстрактным методом get_summary(). Реализуйте наследников
# Post(title, body, author) и Page(title, slug) с super().__init__().
# В get_summary() выведите краткое описание каждого.


class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "06/11/2026"

    @abstractmethod
    def get_summary(self) -> None:
        """Выводит информацию о контенте"""


class Post(Content):
    def __init__(self, title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    @override
    def get_summary(self) -> str:
        return f"Пост {self.title} создан {self.created_at} автором {self.author}."


class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    @override
    def get_summary(self) -> str:
        return f"Дата: {self.created_at}, ссылка: {self.slug}."


if __name__ == '__main__':
    post = Post(title="Как живут манулы", author="Антон", body="Мой первый пост")
    page = Page(title="Что едят манулы", slug="what_eat_manul")

    print(post.get_summary())
    print(page.get_summary())
