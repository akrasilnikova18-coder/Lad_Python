import sys


# Звёздочка (самостоятельное изучение): __slots__ и contextlib.
# Самостоятельно разберитесь:
# в __slots__: перепишите маленький класс (например, Point с двумя координатами)
# на __slots__, объясните, какая экономия памяти и какие ограничения появляются
# (нельзя добавить атрибут p.z). Замерьте разницу в памяти через sys.getsizeof для тысяч объектов.
# в contextlib: найдите @contextmanager и напишите свой контекстный менеджер
# (например, @contextmanager def open_log(...)), который печатает «открыли»/«закрыли»
# при входе в with и выходе из него. Запишите оба вывода комментариями в коде.
# Обе темы более подробно пригодятся в занятии 17.


# Класс без __slots__
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# Класс со __slots__
class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# По классу PointSlots есть ограничение: если я попытаюсь создать
# p.z = 30, он выведет AttributeError, потому что в классе могут быть только аттрибуты,
# которые изначально заданы

# Создаём по 10 000 экземпляров каждого класса
points = [Point(i, i) for i in range(10000)]
points_slots = [PointSlots(i, i) for i in range(10000)]

# Считаем память обычных объектов с учётом __dict__
memory_points = sum(
    sys.getsizeof(p) + sys.getsizeof(p.__dict__)
    for p in points
)

# Считаем память объектов с __slots__
memory_slots = sum(
    sys.getsizeof(p) for p in points_slots
)

print(f"Обычный класс: {memory_points} байт")
print(f"Класс с __slots__: {memory_slots} байт")
print(f"Экономия памяти: {memory_points - memory_slots} байт")
