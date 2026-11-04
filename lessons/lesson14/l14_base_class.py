from typing import override

import ost


class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "04/11/2026"

    def get_summary(self) -> str:
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


post = Post(title="Занимательная алгебра", author="Анна", body="Мой первый пост")
page = Page(title="Занимательная физика", slug="my_first_page")

# print(f"Название: {post.title}, Автор: {post.author}, Текст: {post.body}, Дата: {post.created_at}")
# print(f"Название: {page.title}, Ссылка: {page.slug}")

print(page.get_summary())
print(post.get_summary())
print(Post.__mro__) # порядок наследования
