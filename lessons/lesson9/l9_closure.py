def make_multiplier(multiplicator: int):
    def multiply(number: int) -> int:
        return number * multiplicator
    return multiply

double = make_multiplier(2)
print(double(10))
print(double(50))

tripple = make_multiplier(3)
print(tripple(10))
print(tripple(50))


def make_counter(start: int = 0):
    count = start
    def increment(step: int = 1) -> int:
        nonlocal count
        count += step
        return count
    return increment


counter = make_counter()
print(counter())
print(counter(10)) # 11, потому что в первый раз уже один

new_counter = make_counter(5)
print(new_counter(10))
print(counter()) # 12, потому что второй раз вызываем и step +1
