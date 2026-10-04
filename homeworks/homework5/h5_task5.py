#**Звёздочка (вложенные списки / матрица).** Создайте матрицу 3×4 — список из трёх строк по четыре числа.
# Выведите: а) сумму всех элементов; б) сумму элементов в каждой строке;
# в) максимальный элемент во всей матрице; г) «транспонированную» матрицу (строки и столбцы поменять местами)
# — разберитесь самостоятельно, как это сделать через вложенные циклы и comprehension.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)

#вывести сумму всех элементов и сумму элементов в каждой строке
sum_elements = 0
for row in matrix:
    print(f"Сумма элементов в каждой строке: {sum(row)} ")
    sum_elements += sum(row)

print(f"Сумма всех элементов: {sum_elements}")

#максимальный элемент во всей матрице
max_element = 0
for row in matrix:
    if max(row) > max_element:
        max_element = max(row)

print(f"Максимальный элемент: {max_element}")

#нужно сделать «транспонированную» матрицу (строки и столбцы поменять местами)
zero_elements = []
fist_elements = []
second_elements = []
third_elements = []

for row in matrix:
    zero_elements.append(row[0])
    fist_elements.append(row[1])
    second_elements.append(row[2])
    third_elements.append(row[3])

new_matrix = []
new_matrix.append([zero_elements, fist_elements, second_elements, third_elements])

print(new_matrix)
