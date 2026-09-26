users = ['Илья', 'Мария', 'Анна', 'Сергей']
scores = [95, 88, 79]

print("Список участников: ")
for number, name in enumerate(users):
    print(f"Номер: {number+1}, пользователь: {name}")

print("Результаты по паре: имя и оценка")
for name, score in zip(users, scores):
    print(f"Человек {name} набрал {score} баллов")
