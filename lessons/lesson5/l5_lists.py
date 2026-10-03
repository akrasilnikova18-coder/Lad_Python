categories = []

categories.append("Python")
categories.append("Django")
categories.append("SQL")

categories.extend(["GIT", "Docker"])
categories.insert(0, "Оглавление")

print(categories)
print(len(categories))

print("Django" in categories)
print(categories.count("GIT"))
print(categories.index("Docker"))

first = categories.pop(0)
print(f"Мы удалили элемент {first}")

categories.remove("GIT")
print(categories)
