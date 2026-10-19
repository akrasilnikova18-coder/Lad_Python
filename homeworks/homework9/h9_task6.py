from functools import lru_cache
import time
from itertools import product

"""Звёздочка (продвинутая). Самостоятельное изучение @lru_cache и @property.
Для @lru_cache: найдите его в документации functools и напишите функцию fibonacci с кэшированием,
затем ту же функцию без кэша. Сравните время выполнения для n = 30 (через time.perf_counter())
и объясните комментарием, почему с кэшем быстрее.
Для @property: кратко изучите, как декоратор превращает метод в «свойство»
(доступ obj.field вместо вызова obj.field()). Напишите класс с приватным атрибутом
и свойством-геттером (и, при желании, сеттером), выводящим валидированное значение.
Объясните комментарием, что делает декоратор. Это подготовка к блоку ООП."""


class Product:
    def __init__(self, name: str, price: int):
        """Класс продукта с названием и ценой"""
        self.name = name
        self.price = price


# ГЕТТЕР — возвращает цену
@property
def price(self):
    return self._price


 # СЕТТЕР — проверяет и изменяет цену
@price.setter
def price(self, value):
    if value < 0:
        self._price = 0
        print("Цена не может быть отрицательной")
    else:
        self._price = value


product = Product(name="Ноутбук", price=150000)

print(product.price) # вызывается геттер
product.price = 100000 # вызывается сеттер
print(product.price) # вызывается геттер - проверяем работу сеттера

print(product.name)
product.name = "Ноутбук HP"
print(product.name)
