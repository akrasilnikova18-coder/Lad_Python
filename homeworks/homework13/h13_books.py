# «Библиотека» со классом Book. Класс Book с title, author, year; методы is_old()
# (возвращает True, если книга старше 10 лет) и display().
# Атрибут класса genre = "Художественная литература". Создать 3–4 книги, вывести их и пометить «старые».
# Добавить атрибут класса category_count и объяснить в комментарии разницу между ним и атрибутами экземпляра.


class Book:
    genre = "Художественная литература"
    category_count = 100
    # Атрибут экземпляра у каждого класса свой, например, автор. Атрибут класса общий у всех экземпляров класса.

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        
    def is_old(self) -> bool:
        if self.year < 2016:
            return True
        else:
            return False

    def display(self) -> None:
        print(f"Автор: {self.author}, Название: {self.title}, Жанр: {self.genre}, "
              f"Год издания: {self.year}, Старая: {self.is_old()}")


lord_of_the_rings = Book(title="Властелин Колец", author="Дж.Р.Р.Толкиен", year=2021)
hobbit = Book(title="Хоббит", author="Дж.Р.Р.Толкиен", year=2000)
garry_potter = Book(title="Гарри Поттер и Тайная комната", author="Дж.Роулинг", year=2005)
sherlock_holms = Book(title="Записки о Шерлоке Холмсе", author="Артур Конан Дойл", year=2020)

lord_of_the_rings.is_old()
hobbit.is_old()
garry_potter.is_old()
sherlock_holms.is_old()

lord_of_the_rings.display()
hobbit.display()
garry_potter.display()
sherlock_holms.display()

