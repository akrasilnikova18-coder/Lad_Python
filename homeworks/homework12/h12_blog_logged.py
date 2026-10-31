import json
import logging
from pathlib import Path
from json import JSONDecodeError


# Безопасное чтение постов. Напишите функцию load_posts,
# которая читает JSON-файл постов и: возвращает пустой список, если файла нет (FileNotFoundError);
# при битом JSON (json.JSONDecodeError) — логирует ошибку и пробрасывает исключение raise
# (не «притворяясь», что всё хорошо). Подсказка: используйте logging и Path.

POSTS_FILE = Path("articles.json")

# настраиваем логгер
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger("blog") # получаем объект логгера


def load_posts() -> list:
    try:
        with POSTS_FILE.open(encoding="utf-8") as f:
            posts = json.load(f)
            print(f"В файле {POSTS_FILE} {len(posts)} строк.")
            return posts

    except FileNotFoundError:
        logger.error(f"Файл {POSTS_FILE} не найден. Возвращаю пустой список.")
        return []
    
    except json.decoder.JSONDecodeError as e:
        logger.error(f"Битый JSON в файле {POSTS_FILE}. Ошибка: {e}")
        raise
    
    
if __name__ == "__main__":
    try:
        load_posts()
        
    except JSONDecodeError:
        print("Файл поврежден, попробуйте снова.")
