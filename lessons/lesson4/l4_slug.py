def built_slug(title: str) -> str:
    result = title.lower()
    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    result = result.strip('-')
    return result

new_text = "Занимательная алгебра, геометрия и все-все-все!!! % И еще много всего!"
print(new_text)
print(built_slug(new_text))