from collections import namedtuple


Person = namedtuple("Person", ["name", "age", "city"])
ivan = Person("Ivan", 25, "Moskow")
anna = Person(name="Anna", age=20, city="Moskow")

print(ivan.name)
print(anna.age)
print(ivan)

print(Person._fields)

print(ivan._asdict())

ivan_next_year = ivan._replace(age=26)
print(f"Сейчас Ивану {ivan.age}, через год будет {ivan_next_year.age}")
