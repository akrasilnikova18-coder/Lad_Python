import json
from pathlib import Path


POSTS_FILE = Path("posts.json")

if __name__ == "__main__":

    def read_posts(path: Path) -> list:
        try:
            with path.open(encoding="utf-8") as f:
                data = json.load(f)

        except FileNotFoundError:
            print(f"Такого файла нет: {path}")
            data = []

        else:
            print(f"Файл {path} открыт, количество записей в файле {len(data)}")

        finally:
            print("Чтение файла завершено")

        return data

    read_posts(POSTS_FILE)
