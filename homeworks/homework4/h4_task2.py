#Красивый заголовок. На вход подаётся «грязный» заголовок с лишними пробелами, кавычками
# и знаками препинания. «Почистить» его: убрать краевые пробелы (strip),
# схлопнуть повторные пробелы (split + join), снять фигурные скобки/кавычки (replace)
# и перевести каждое слово с заглавной буквы (capitalize в цикле). Вывести аккуратный заголовок.

dirty = " Текст   про   большого!!! пушистого %, толстого :) манула!!    "

#убираем пробелы с начала и с конца, переводим строку в список
new_text = dirty.strip()
words_list = new_text.split()

#каждое слово начинаем с заглавной буквы
capital = []
for word in words_list:
    capital.append(word.capitalize())

new_text = " ".join(capital)

#убираем лишние значения - по итогам убралось все, кроме запятой перед пробелом
clean = []
for char in new_text:
    if char == "!" or char == "%" or char == ")" or char == ":" or char == "  ":
        clean.append("")
    else:
        clean.append(char)

new_text = "".join(clean)

#убираем запятую с пробелом
new_text = new_text.replace(' ,', ',')
print(new_text)
