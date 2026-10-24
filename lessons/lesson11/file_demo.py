file = open("notes.txt", "w", encoding="utf-8")
file.write("Моя первая заметка\n")
file.write("Моя вторая заметка\n")
file.close()


with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)


with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Дополнительно: третья заметка\n")


with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"Строка: {line.strip()}")
