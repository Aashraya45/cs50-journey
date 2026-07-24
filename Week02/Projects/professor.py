import random
problems = []
answers = []
def main():
    score = 0
    life = 3
    n = get_level()
    for _ in range(1,11):
        x = generate_integer(n)
        y = generate_integer(n)
        answers.append(x+y)
        problems.append(f"{x}+{y} = ")
    for problem in range(len(problems)):
        while True:
            if life!=0:
                answer = input(problems[problem])
                try:
                    if int(answer) == answers[problem]:
                        score+=1
                        life = 3 
                        break
                    elif int(answer) != answers[problem]:
                        life-=1
                        print("EEE")
                        continue
                except ValueError:
                    life-=1
                    print("EEE")
                    continue
            else:
                print(f"{problems[problem]}{answers[problem]}")
                life = 3
                break   
    print(f"Score: {score}")      
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError
    
if __name__ == "__main__":
    main()