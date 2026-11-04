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


def show(item: Content) -> None:
    print(item.get_summary())


post = Post(title="Занимательная алгебра", author="Анна", body="Мой первый пост")
page = Page(title="Занимательная физика", slug="my_first_page")

print(page.get_summary())

items = [post, page]
for item in items:
    show(item)
