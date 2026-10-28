import json
import logging
from json import JSONDecodeError
from pathlib import Path
from l12_validation import ValidationError
from l12_try_finally import POSTS_FILE


# настраиваем логгер
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger("blog") # получаем объект логгера


def load_posts() -> list:
    if not POSTS_FILE.exists():
        logger.info(f"Файл {POSTS_FILE} не найден. Возвращаем пустой список.")
        return []

    try:
        with POSTS_FILE.open(encoding="utf-8") as f:
            return json.load(f)

    except json.decoder.JSONDecodeError as e:
        logger.error(f"Битый JSON в файле {POSTS_FILE}. Ошибка: {e}")
        raise


def safe_post(post: list) -> None:
    with POSTS_FILE.open(mode="w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=2)

    logger.info(f"Сохранено {len(post)}")


def add_post(title: str, body: str) -> dict:
    if not title.strip() or not body.strip():
        raise ValidationError("Заголовок или текст не должны быть пустыми")

    posts = load_posts()
    post = {"title": title, "body": body,}
    posts.append(post)

    safe_post(posts)
    return post


def lists_posts() -> None:
    posts = load_posts()

    if not posts:
        print("Постов пока нет")
        return

    for num, post in enumerate(posts, start=1):
        print(f"{num}. {post['title']} - {post['body']}")

       

if __name__ == "__main__":
    while True:
        logger.info("Программа начала работу")
        
        print(
            """
            Выберите действие:
            add - Добавить пост
            list - Показать посты
            exit - Выход
            """
        )

        action = input("Введите команду ").strip().lower()

        if action == "add":
            title = input("Введите название статьи ").strip()
            body = input("Введите текст статьи ").strip()

            try:
                add_post(title, body)

            except ValidationError as e:
                logger.warning(f"Некорректный ввод: {e}")
                print(f"Ошибка. Попробуйте снова. \n{e}")
                continue

            except JSONDecodeError:
                print("Файл поврежден, попробуйте снова.")
                continue

            else:
                print("Пост добавлен")

        elif action == "list":
            
            try:
                lists_posts()

            except JSONDecodeError:
                print("Файл поврежден, попробуйте снова.")
                continue

            except KeyError as e:
                logger.error(f"В файле {POSTS_FILE} неправильная структура данных: {e}")
                print("Некорректный тип файла")
                continue
                
        elif action == "exit":
            logger.info("Программа завершила работу")
            print("Завершение работы")
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")

