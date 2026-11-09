from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date


# ⭐⭐ Звёздочка (самостоятельное изучение abc и dataclasses).
# По официальной документации Python изучите (https://docs.python.org/3/library/abc.html
# и https://docs.python.org/3/library/dataclasses.html):
# (а) чем ABC отличается от обычного класса,
# (б) зачем нужен @abstractmethod,
# (в) как @dataclass упростил бы ваши классы Post/Page (поля, __init__, __repr__ — без ручного кода).
# Напишите конспект на 5–8 предложений с примером кода, где Content описан через @dataclass,
# и сравните с ручной версией. Это задел на следующее занятие.


"""ABC (Abstract Base Class) — это абстрактный базовый класс, который, в отличие от обычного класса,
позволяет задавать обязательные методы для дочерних классов.
Обычный класс можно создавать и использовать напрямую, а экземпляр абстрактного класса нельзя создать,
пока в нём остаются нереализованные абстрактные методы.
Декоратор @abstractmethod нужен, чтобы указать методы, которые обязательно должны быть реализованы
в конкретных дочерних классах.
Декоратор @dataclass позволяет сократить количество кода, автоматически
создавая методы __init__(), __repr__() и __eq__().
Вместо ручного написания конструктора и присваивания значений атрибутам достаточно перечислить
поля класса с аннотациями типов.
Это удобно, поскольку уменьшает дублирование кода и делает его более понятным."""


@dataclass
class Content(ABC):
    title: str

    @abstractmethod
    def get_summary(self) -> str:
        """Выводит информацию о тексте"""


@dataclass
class Post(Content):
    author: str
    text: str

    def get_summary(self) -> str:
        return f"Статья: {self.title}, автор: {self.author}"


@dataclass
class Page(Content):
    slug: str

    def get_summary(self):
        return f"Страница: {self.title}, адрес: {self.slug}"


post = Post(title="Python", author="Анна", text="Изучаем ООП")
page = Page(title="Главная", slug="/home")

print(post)
print(post.get_summary())
print(page.get_summary())
