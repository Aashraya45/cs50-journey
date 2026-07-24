import inflect
names = []
p = inflect.engine()
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)
sentence = p.join(names)
print(f"Adieu, adieu, to {sentence}")