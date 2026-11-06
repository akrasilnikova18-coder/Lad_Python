# Звёздочка (множественное наследование и MRO). Создайте два миксина
# (TagMixin с add_tag(), Loggable с log()) и класс Post(TagMixin, Loggable, Content)
# — миксины первыми, базовый класс последним. Напечатайте Post.__mro__ — посмотрите порядок.
# Поэкспериментируйте: поменяйте порядок миксинов в объявлении класса и объясните,
# как изменится результат выполнения (что победит при совпадении имён методов).
# Запишите вывод комментарием.


class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "06/11/2026"

    def get_summary(self) -> str:
        """Выводит информацию о контенте"""
        return f"Пост {self.title} создан {self.created_at}"


class TagMixin:
    def add_tag(self, tag):
        if not hasattr(self, "tags"):
            self.tags = []
        self.tags.append(tag)
        return self


class Loggable:
    def log(self, message):
        print(f"[LOG] {message}")


# Если сначала будет Content, то TagMixin и Loggable работать не будут, так как MRO читается слева направо
# Если первым будет базовый класс, то будут использоваться только его методы
class Post(TagMixin, Loggable, Content):
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
        

if __name__ == "__main__":
    print(Post.__mro__ )