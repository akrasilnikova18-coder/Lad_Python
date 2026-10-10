point = (10, 20)
colors = 'green', 'red', 'green', 'blue' #это тоже кортеж, скобки не обязательны

single = (5,)
print(type(single))

no_tuple = 5
print(type(no_tuple))

print(len(colors))

print(colors[0])
print(colors[-1])
print(colors[1::])

print(f"Есть ли красный? {'red' in colors}?")

if 'green' in colors:
    print(colors.index('green'))
    print(colors.count('green'))

try:
    colors[0] = 'black'
except TypeError as err:
    print(f"Нельзя изменить кортеж {err}")
