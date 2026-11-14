from contextlib import contextmanager
from typing import Generator


@contextmanager
def open_file(path: str, mode: str = "r") -> Generator:
    file = open(path, mode, encoding="utf-8")
    try:
        yield file
    finally:
        file.close()
        print("Файл закрыт")


@contextmanager
def timer(label: str) -> None:
    import time
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} - {elapsed:.4f}")


if __name__ == '__main__':
    with open_file("test.txt", "w") as file:
        file.write("Первая строка\n")
        file.write("Вторая строка\n")

    with open_file(path="test.txt") as file:
        print(file.read())

    with timer("Ожидание от цикла"):
        for _ in range(1_000_000):
            pass
