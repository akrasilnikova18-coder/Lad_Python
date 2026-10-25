import json
from pathlib import Path


# «Блог CLI» (мини-проект). Доработать утилиту blog_cli.py: добавить сохранение нескольких полей статьи
# (заголовок, автор, содержание) и вывод красиво отформатированного списка статей при каждом запуске.
# Проверить, что данные переживают перезапуск программы.

# Звёздочка (работа с путями, pathlib). Переписать программу из задачи 4 так, чтобы файл статьи сохранялся в подпапке проекта.
# Например, создайте папку data/ через Path("data").mkdir(exist_ok=True) и сохраняйте data/articles.json.
# Убедитесь, что при запуске из любой папки программа находит свой файл.
# Используйте Path.cwd() для понимания, откуда запускается скрипт.


# Папка, в которой находится сам скрипт
BASE_DIR = Path(__file__).resolve().parent

# Создаем папку data, если ее еще нет
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Путь к файлу со статьями
DATA_FILE = DATA_DIR / "articles.json"

print("Текущая рабочая папка:", Path.cwd())

def load_articles() -> list:
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
        print("Ошибка: файл JSON пустой или содержит некорректные данные")
        return []
    
def save_articles(articles: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print("Статьи записаны в:", DATA_FILE.resolve())
    print("Размер файла:", DATA_FILE.stat().st_size, "байт")

    print("Проверка сохранения:")
    print(load_articles())


def main() -> None:
    articles = load_articles()
    title = input("Введите название статьи ")
    author = input("Введите автора ")
    text = input("Введите текст статьи ")
    new_post = {
        "title": title,
        "author": author,
        "text": text
    }

    articles.append(new_post)
    save_articles(articles)
    print("Статья сохранена")

    print("\nТекущий список статей:")
    for num, article in enumerate(articles, start=1):
        print(f"{num}. {article['title']} - {article['author']} - {article['text']}")


if __name__ == "__main__":
    main()