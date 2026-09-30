title = "Занимательная геометрия"

print(title[4])
print(title[-2])
print(title[7:])

print(title[14:])
print(title[::-1])

print(title.upper())
print(title.lower())

dirty = "% теорема "
clean = dirty.strip('%, ')
print(clean)

print(f"Длина до strip {len(dirty)}, после strip {len(clean)}")

print(title.replace("геометрия", "математика"))
print(title.replace("я", "а"))

print(title.startswith("З"), title.endswith("геометрия"))
print(title.find("геометрия"))
print(title.count("а"))
