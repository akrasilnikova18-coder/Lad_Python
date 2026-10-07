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

new_row = []
new_matrix = []

#нужно сделать «транспонированную» матрицу (строки и столбцы поменять местами
for i in range (0, len(matrix[0])):
    for j in range (0, len(matrix)):
        new_row.append(matrix[j][i])
print(new_row)

new_rows = len(matrix[0]) #должно быть 4 строки, так как у матрицы было 4 столбца
new_cols = len(matrix) #должно быть 3 столбца, так как у матрицы было 3 строки

new_matrix = [[new_row[i*new_cols + j] for j in range(new_cols)] for i in range(new_rows)]
print(new_matrix)
