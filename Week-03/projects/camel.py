capitals = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

variable = input("camelCase: ")

for i in range(len(variable)):
    for j in range(26): 
        if variable[i] == capitals[j]:
            variable = variable[0:i] + "_" + variable[i].lower() + variable[i+1:]

print(variable)
        

