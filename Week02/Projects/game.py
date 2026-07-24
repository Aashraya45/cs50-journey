import random
overall = True
mini = True
while overall and mini:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        overall= False
        if n>0:
            number = random.randint(1, n) 
        while mini:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                pass
            else:
                if n>0:
                    if guess>number:
                        print("Too large")
                    elif number>guess:
                        print("Too small")
                    else:
                        print("Just right!")
                        mini=False
                else:
                    raise ValueError
            
        else:
            raise ValueError