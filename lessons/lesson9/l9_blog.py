import time
import functools


articles = [
    {"id": 1, "title": "C++", "author": "Anna"},
    {"id": 2, "title": "Python", "author": "Bob"},
    {"id": 3, "title": "Django", "author": "Maikl"},
]


def time_it(func):
    @functools.wraps(func) # для сохранения метаданных
    def wrapper(*args, **kwargs): # можно передавать любые аргументы
        start = time.perf_counter()
        result = func(*args, **kwargs) # выполняется переданная функция
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработала за {elapsed:.6f} секунд") # не более 6 знаков после точки
        return result
    return wrapper


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Результат: {func.__name__} - {result}")
        return result
    return wrapper


@logged
@time_it
def list_articles() -> str:
    for article in articles:
        print(f"({article['id']}): {article['title']} - {article['author']})")

    return f"Всего статей: {len(articles)}"


@logged
def add_article(title: str, author: str) -> str:
    new_id = max(article["id"] for article in articles) + 1
    new_article = {"id": new_id, "title": title, "author": author}
    articles.append(new_article)
    return f"Добавлена статья с id {new_id}"


@logged
def find_article(article_id: int) -> str | None:
    for article in articles:
        if article["id"] == article_id:
            return article["title"]
        return None


list_articles()
add_article(title="Java", author="Alex")
list_articles()
find_article(3)
