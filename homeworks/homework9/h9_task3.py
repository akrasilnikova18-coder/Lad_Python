import functools
import time


"""Один декоратор — на несколько функций. Напишите декоратор @logged (или @time_it)
и примените его сразу к трём функциям «блога»: create_article, get_article_by_id, delete_article.
Заготовки функций сделайте простыми (работа с тем же списком статей в памяти),
чтобы поведение добавлял именно декоратор. Поясните комментарием, что изменилось бы,
если бы пришлось вставлять логирование в тело каждой функции вручную."""

articles = [
    {"id": 1, "title": "C++", "author": "Anna"},
    {"id": 2, "title": "Python", "author": "Bob"},
    {"id": 3, "title": "Django", "author": "Maikl"},
]


def time_it(func):
    """Декоратор считает время выполнения функции"""

    @functools.wraps(func) # для сохранения метатегов функции
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Функция {func.__name__} отработала за {end - start:.6f} с.")
        return result

    return wrapper

@time_it
def create_article(author: str, title: str):
    """Добавляет новую статью"""
    new_id = max(post["id"] for post in articles) + 1
    new_post = {"id": new_id, "title": title, "author": author}
    articles.append(new_post)
    return f"Добавлена новая статья с id: {new_id}"


@time_it
def get_article_by_id(article_id: int):
    """Выводит название статьи по id или None, если не нашел"""
    for post in articles:
        if post["id"] == article_id:
            return f"Найдена статья с названием: {post["title"]}"
    return None

@time_it
def delete_article(article_id):
    "Удаляет статью"
    for post in articles:
        if post["id"] == article_id:
            deleted_article = articles.pop(article_id)

    return f"Удалена статья с названием: {deleted_article["title"]}"


create_article(author="Alina", title="Java")
get_article_by_id(2)
delete_article(1)

# Если бы пришлось вставлять отсчет времени работы функции в каждую функцию, то это лишние строки кода
# И, если что-то нужно изменить, пришлось бы менять в коде каждой из трех функций