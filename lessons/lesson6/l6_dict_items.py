scores = {
    "Python": 90,
    "Django": 85,
    "Postgres": 60,
}

for course in scores:
    print(course)

for score in scores.values():
    print(score)

for course, score in scores.items():
    print(f"{course}: {score}")

total = 0

for score in scores.values():
    total += score

print(f"Сумма всех баллов: {total}")

print(scores.get("Flask", "Курса нет"))
print(scores.get("Django", "Курса нет"))
