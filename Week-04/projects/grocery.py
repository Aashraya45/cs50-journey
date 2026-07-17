items = {}
while True:
    try:
        item = input("Item: ").upper()
    except EOFError:
        for i in items:
            print(f"{items[i]} {i}")
            break
    else:
        if item in sorted(items):
            items[item]+=1
        else:
            items[item]=1
