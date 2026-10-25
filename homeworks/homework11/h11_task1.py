#Заметки. Создать программу, которая принимает от пользователя текст и дописывает его в файл notes.txt
# (режим "a"), а затем читает весь файл и выводит его с номерами строк.


with open("notes.txt", "a", encoding="utf-8") as f:
    note = input("Введите заметку для записи ")
    f.write(note + "\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    for num, note in enumerate(f.readlines(), start=1):
        print(f"{num}. {note}")
