import json
from pathlib import Path
import logging


# Свои исключения в «Блог CLI». Расширьте утилиту блога: добавьте class PostNotFoundError(Exception)
# и функцию get_post(index), которая возвращает пост по номеру; если такого поста нет — бросает
# PostNotFoundError. В сценарии list обработайте её так, чтобы пользователь видел «Пост № N не найден».
# Убедитесь, что чужие ошибки (например, IndexError) не попадают в этот обработчик.

# Звёздочка (логирование). Замените все print() в утилите блога на логирование через logging:
# INFO для «обычных» событий, WARNING для предупреждений, ERROR для ошибок.
# Настройте basicConfig с форматом %(asctime)s | %(levelname)s | %(message)s.
# Добейтесь, чтобы при «обычной» работе выводились только INFO, а при сбое — ERROR в журнал.
# Объясните в комментарии, зачем logging лучше print().

POSTS_FILE = Path("articles.json")

class PostNotFoundError(Exception):
    """Ошибка в поиске поста по номеру"""
    
    
# настраиваем логгер
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("blog") # получаем объект логгера


def load_articles() -> list:
    if not POSTS_FILE:
        logger.info(f"Файл {POSTS_FILE} не найден. Возвращаем пустой список.")
        return []
    
    try:
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            logger.info(f"Открыли файл: {POSTS_FILE}")
            return json.load(f)
        
    except:
        logger.error("Ошибка: файл JSON пустой или содержит некорректные данные")
        return []


def save_articles(articles: list) -> None:
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)


def get_post(index: int):
    with open(POSTS_FILE, "r", encoding="utf-8") as f:
        articles = json.load(f)

    if index > len(articles):
        raise PostNotFoundError(f"Пост с номером {index} не найден.")

    for num, article in enumerate(articles, start=1):
        if num == index:
            logger.info(f"Найден пост: {article['title']}")
            print(f"Найден пост под номером: {num}. {article['title']} - {article['author']} - {article['text']}")


def main() -> None:
    logger.info("Программа начала работу")
    
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
    logger.info("Статья сохранена")

    print("\nТекущий список статей:")
    for num, article in enumerate(articles, start=1):
        print(f"{num}. {article['title']} - {article['author']} - {article['text']}")

    find_index = int(input("Введите номер поста "))

    try:
        get_post(find_index)
    except PostNotFoundError as e:
        logger.error(f"Не удалось найти пост, ошибка: {e}")

    logger.info("Программа завершила работу")


if __name__ == "__main__":
    main()

# print выводит информацию, но не сохраняет ее, а logger можно сохранить и проанализировать
# потом в logger есть дополнительная информация, время начала и окончания программы, например