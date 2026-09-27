#**Только чётные.** Вывести все **чётные** числа от 1 до 100
# через `for` в сочетании с `range` и `continue` (нечётные пропускать).

for number in range(1, 101):
    if number % 2 == 0:
        print(f"Четное число: {number}")
        continue