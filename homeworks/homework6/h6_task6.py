def unique_elements(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

original = ["b", "a", "b", "c", "a"]
unique_list = unique_elements(original)
print(unique_list)

number_list = [6, 7, 5, 7, 3, 3, 7, 8]
unique_list = unique_elements(number_list)
print(unique_list)

from collections import OrderedDict

# OrderedDict — это упорядоченный словарь из модуля collections.
# Он сохраняет порядок добавления элементов.
# Нужен, когда важно не только хранить данные, но и менять их порядок.
# Начиная с Python 3.7, обычный dict тоже сохраняет порядок добавления.
# Отличие OrderedDict — наличие дополнительных методов для управления порядком элементов.
# Также при сравнении двух OrderedDict учитывается порядок ключей.
# То есть ту же задачу можно было решить через OrderedDict

def remove_duplicates(items):
    return list(OrderedDict.fromkeys(items))

items = ["b", "a", "b", "c", "a"]
print(remove_duplicates(items))

# Результат: ['b', 'a', 'c']