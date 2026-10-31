import json
from pathlib import Path


# Звёздочка (повышенная сложность). Изучите по официальной документации Python цепочку исключений —
# конструкцию raise ... from e — и иерархию встроенных исключений (от BaseException до Exception и ниже).
# Приведите в комментарии пример, где raise NewError from original_error полезен (сохранить исходную причину),
# и коротко опишите, какие типы исключений стоит ловить, а какие — нет
# (например, зачем избегать except BaseException и слепого except:).


# Цепочка исключений (raise ... from e) позволяет вызвать новую ошибку, сохранив первоначальную причину.
# Например, если программа не смогла открыть файл из-за FileNotFoundError, можно вызвать собственное
# исключение PostError через raise PostError(...) from e. Это помогает понять, из-за чего возникла ошибка.
#
# Лучше перехватывать конкретные исключения, например except FileNotFoundError или except ValueError.
# Лучше не использовать except BaseException и пустой except:, потому что они перехватывают
# даже KeyboardInterrupt и SystemExit. Это может мешать корректному завершению программы.

# Пример цепочки исключений:

class PostError(Exception):
    """Ошибка: файл не найден"""

POSTS_FILE = Path("articles.json")


def load_posts() -> list:
    try:
        with POSTS_FILE.open(encoding="utf-8") as f:
            posts = json.load(f)
            print(f"Количество строк в файле: {len(posts)}")
            return posts

    except FileNotFoundError as e:
        raise PostError("Файл со статьями не найден") from e


if __name__ == "__main__":
    try:
        load_posts()
    except PostError as e:
        print(f"Не удалось открыть файл. Ошибка: {e}")
