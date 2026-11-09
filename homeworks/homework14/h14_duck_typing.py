# Полиморфизм и duck typing. Напишите функцию render_all(items), которая принимает список объектов
# и вызывает у каждого get_summary(). Заполните список постами и страницами и выведите результат.
# Затем дополнительно передайте в неё объект, который не наследуется от Content, но имеет метод
# get_summary() (например, класс с __getattr__/собственным get_summary()), — и покажите,
# что функция его тоже принимает. Это демонстрация duck typing.


class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "06/11/2026"

    def get_summary(self) -> str:
        """Выводит информацию о контенте"""
        return f"Пост {self.title} создан {self.created_at}"


class Post(Content):
    def __init__(self, title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    def get_summary(self) -> str:
        info = super().get_summary()
        return f"{info}, количество знаков в посте {len(self.body)}."


class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    def get_summary(self) -> str:
        return f"Дата: {self.created_at}, ссылка: {self.slug}."
    

class Blog:
    def __init__(self, title: str, text: str) -> None:
        self.title = title
        self.text = text

    def get_summary(self) -> str:
        return f"Мой первый пост - {self.text}"


def render_all(items: list[Content]) -> None:
    for item in items:
        print(item.get_summary())


if __name__ == '__main__':
    texts = [
        Post(
            title="Как живут манулы",
            author="Антон",
            body="Мой первый пост. Мой второй пост",
        ),
        Page(title="Что едят манулы", slug="what_eat_manul"),
        Post(
            title="Слоны в Московском зоопарке",
            author="Ирина",
            body="Мой третий пост",
        ),
        Page(title="О пингвинах", slug="about_pingvin"),
        Blog(title="Панды в Московском зоопарке", text="Блог про панд"),
        Blog(title="И другие медведи", text="Блог про других медведей"),
    ]

    render_all(texts)
