class Post:
    def __init__(self, title: str, author: str, text: str) -> None:
        self.title = title
        self.author = author
        self.text = text
        self.likes = 0


first = Post(title="Занимательная физика", author="Алла", text="Мой первый пост. Мой второй пост.")
second = Post(title="Занимательная математика", author="Игорь", text="Мой третий пост. Мой четвертый пост.")


print(first.title)
print(second.title)
print(second.likes)

print(first is second) # == сравнивает значения, а is - разные объекты = положение в памяти

print(type(first)) # __main__ - имя модуля, где есть этот класс, если бы был импорт, было бы название файла, откуда импорт
print(type(second))
