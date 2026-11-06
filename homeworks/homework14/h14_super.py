# Переопределение и super(). Для Post переопределите get_summary(),
# дополнив родительскую версию через super() (например, добавьте длину текста).
# Для Page — верните полностью свою реализацию. Вызовите метод у экземпляров обоих классов
# и сравните вывод.

# Связь наследования и Django. Напишите 2–3 предложения (комментарием в коде или в отдельном .md),
# почему CBV в Django строятся на наследовании и super() — приведите пример class MyView(ListView).
# Свяжите с тем, что вы делали в этапе 1–3.

# CBV в Django строятся на наследовании, чтобы можно было использовать
# готовую логику родительских классов и изменять только нужные методы.
# super() позволяет вызвать метод родительского класса, сохранив его функциональность.
# Это связано с этапами 1–3, где мы изучали классы, наследование и переопределение методов.
# Например, class MyView(ListView) - это готовый класс Django, который умеет получать список объектов
# То есть можем его вызвать и переопределить нужные методы


"""
class MyView(ListView):
    model = Article
    template_name = "articles.html"

    def get_queryset(self):
        queryset = super().get_queryset() - вызываем реализацию родительского метода, которая получает исходный набор объектов.
        return queryset.filter(is_published=True) - добавляем собственную логику: показываем только опубликованные статьи.
"""


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


if __name__ == '__main__':
    post = Post(title="Как живут манулы", author="Антон", body="Мой первый пост. Мой второй пост")
    page = Page(title="Что едят манулы", slug="what_eat_manul")

    print(post.get_summary())
    print(page.get_summary())
