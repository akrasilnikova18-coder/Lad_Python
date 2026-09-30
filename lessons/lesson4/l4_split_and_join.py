text = "Занимательная    геометрия  и    математика"
words = text.split()
print(words)

print(f"Слов в тексте: {len(words)}")

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Самое длинное слово - {longest}")

new_text = " | ".join(words)
print(new_text)

normalized = " ".join(text.split())
print(normalized)

print(f"Символов до очистки: {len(text)}")
print(f"Символов после очистки: {len(normalized)}")
