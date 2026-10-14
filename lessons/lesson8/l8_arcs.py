def sum_all(*numbers: int) -> int:
    """Складывает произвольное количество чисел"""
    total = 0
    for number in numbers:
        total += number
    return total


def print_config(**kwargs: dict[str, str]) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print(sum_all(1, 2, 3, 4, 5, 6))
print_config(key="Ivan", value="25", age="20")


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

articles = [
    {"title": "Python", "rating": 4.5},
    {"title": "Java", "rating": 2.5},
    {"title": "C++", "rating": 5.5},
]

by_rating = sorted(articles, key=lambda x: x["rating"])
print(by_rating)
