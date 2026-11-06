from typing import Protocol, runtime_checkable


# ⭐⭐ Звёздочка (Protocol вместо ABC). Возьмите контракт из задания 1 (метод get_summary())
# и опишите его как Protocol (class Summarizable(Protocol)).
# Покажите, что Post и Page удовлетворяют протоколу без наследования от него,
# а функция render_all(items: list[Summarizable]) корректно их принимает.
# Добавьте @runtime_checkable и проверьте isinstance(Post(), Summarizable).
# В комментариях объясните, в чём выгода Protocol перед ABC именно в этом случае.
# Посмотрите в typing (https://docs.python.org/3/library/typing.html) раздел про Protocol.


@runtime_checkable
class Summarizable(Protocol):
    def get_summary(self) -> str:
        ...


class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "06/11/2026"


class Post(Content):
    def __init__(self, title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    def get_summary(self) -> str:
        return f"Пост {self.title} создан {self.created_at} автором {self.author}."


class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    def get_summary(self) -> str:
        return f"Дата: {self.created_at}, ссылка: {self.slug}."


def render_all(items: list[Summarizable]) -> None:
    for item in items:
        print(item.get_summary())


if __name__ == "__main__":
    post = Post(
        title="Как живут манулы",
        author="Антон",
        body="Мой первый пост"
    )
    page = Page(
        title="Что едят манулы",
        slug="what_eat_manul"
    )

    render_all([post, page])

    print(isinstance(post, Summarizable))
