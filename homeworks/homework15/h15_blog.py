from dataclasses import dataclass, field


# «Красивый список постов». В файле blog.py дополните классы Author, Post, Category
# методами __str__ и __repr__ (как в Этапе 1). Соберите в main.py блог из 3–4 постов,
# разбейте на пару категорий (например, «Новости», «IT») и выведите каждую категорию
# отдельным аккуратным блоком. Убедитесь, что print(post) и print(posts) дают разный вывод —
# и коротко комментарием в коде объясните, почему.

# Контролируемая модель поста». Перепишите Post так, чтобы заголовок хранился в self._title,
# а наружу отдавался через @property с сеттером-валидацией (не пустой, обрезка пробелов).
# Добавьте вычисляемые свойства: title_length (длина заголовка)
# и slug (заголовок в нижнем регистре, пробелы → дефисы; например, «Мой Первый Пост» → мой-первый-пост).
# Продемонстрируйте, что запись пустого заголовка поднимает ValueError.

# «dataclass для комментариев». Создайте @dataclass class Comment с полями author, text, likes=0 и tags
# (через field(default_factory=list)). Добавьте классу __post_init__: если text пустой — выбрасывать
# ValueError (дополнительная валидация после авто-__init__).
# Проверьте, что: (а) Comment("А", "X") == Comment("А", "X") — True;
# (б) тег, добавленный в один комментарий, не «протекает» в другой.

# Звёздочка: __eq__ + __hash__. Изучите, как переопределить __eq__ и __hash__ вместе
# (см. документацию Python по разделу emulating hashable types). Сделайте так, чтобы Post
# сравнивался по заголовку (__eq__), а также мог быть ключом словаря / элементом множества (__hash__),
# согласованно: у равных объектов — равные hash. Проверьте: {post1, post2} не выбросит TypeError:
# unhashable type, а два поста с одинаковым заголовком «склеятся» в один элемент множества.


class Author:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    @classmethod
    def from_csv(cls, row: str) -> Author:
        name, email = row.split(";")
        return cls(name, email)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Author(name={self.name!r}, email={self.email!r})"


class Category:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Category(title={self.title!r})"


class Post:
    def __init__(self, title: str, text: str, author: Author, category: Category) -> None:
        self._title = title
        self.text = text
        self.author = author
        self.category = category
        
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Заголовок не может быть пустым.")
        self._title = value

    @property
    def title_length(self) -> int:
        return len(self._title)

    @property
    def slug(self) -> str:
        return self._title.lower().replace(" ", "-")

    def __str__(self) -> str:
        return f"{self._title} — {self.author.name}"

    def __repr__(self) -> str:
        return (
            f"Post(title={self._title!r}, "
            f"text={self.text!r}, "
            f"author={self.author!r}, "
            f"category={self.category!r})"
        )

    def display(self):
        print(
            f"Категория: {self.category}, "
            f"Название: {self._title}, "
            f"Автор: {self.author.name}"
        )

    @staticmethod
    def is_valid_text(text: str) -> bool:
        return isinstance(text, str) and bool(text.strip())

    @staticmethod
    def find_for_category(posts: list, category: str) -> None:
        found = False

        for post in posts:
            if post.category.title == category:
                post.display()
                found = True

        if not found:
            print(f"Постов в категории {category} не найдено.")

    # Сравнивает два объекта. Если второй объект не является экземпляром Post, возвращается NotImplemented
    # Сравниваем только заголовки. Если они совпадают, объекты считаются равными
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Post):
            return NotImplemented
        return self.title == other.title

    # Функция hash() вычисляет хеш-значение заголовка — целое число, которое Python использует при работе со словарями и множествами.
    # Поскольку __eq__ сравнивает посты только по заголовку, __hash__ тоже должен использовать только заголовок.
    # Главное правило:
    # Если post1 == post2 возвращает True, то hash(post1) == hash(post2) обязательно должно быть True.
    # Обратное правило не действует: одинаковые хеши не обязательно означают равенство объектов.
    def __hash__(self) -> int:
        return hash(self.title)


@dataclass
class Comment:
    author: str
    text: str
    likes: int = 0
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.text:
            raise ValueError("Текст пустой")

    def __str__(self) -> str:
        return f"Автор: {self.author}, Текст: {self.text}, Теги: {self.tags}, Лайки: {self.likes}"
