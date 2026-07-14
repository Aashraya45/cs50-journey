vowels = ["a", "e", "i", "o", "u"]
answer = input("Input: ")
output = ""
for letter in answer:
    if letter.lower() not in vowels:
        output += letter
print(f"Output: {output}")