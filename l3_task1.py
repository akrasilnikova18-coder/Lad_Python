total = 0
for number in range(1, 6):
    cube = number ** 3
    print(f"Число {number} в кубе = {cube}")
    total += cube

print(f"Сумма всех кубов: {total}")
