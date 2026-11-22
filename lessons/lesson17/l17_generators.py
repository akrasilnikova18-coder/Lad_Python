from typing import Generator
from itertools import chain


def redlines(filename: str) -> Generator[str]:
    with open(filename, encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def squares(number: int) -> Generator[int]:
    for num in range(number):  # noqa: F821
        yield num*num


if __name__ == '__main__':
    # for num in squares(10):
        # print(num)

    # print(list(squares(10)))

    with open("test.txt", "w", encoding="utf-8") as f:
        for num in squares(10):
            f.write(f"Этот квадрат {num}\n")

    for line in redlines("test.txt"):
        if "6" in line:
            print(line)

    line1 = list(squares(10))
    line2 = tuple(squares(10))
    line3 = list(squares(50))

    for element in chain(line1, line2, line3):
        print(element)

