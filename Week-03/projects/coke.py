Due = 50
paid = 0
while Due > paid:
    print(f"Amount Due: {Due-paid}")
    user_input = int(input("Insert coin: "))
    if user_input == 25 or user_input == 10 or user_input == 5:
        paid+=user_input

print(f"change owed: {paid - Due}") 