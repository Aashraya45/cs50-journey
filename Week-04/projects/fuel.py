while True:
    try:
        fraction = input("Fraction: ").split("/")
        if int(fraction[0]) <= int(fraction[1]) and int(fraction[0])>=0 and int(fraction[1])>0:
            percentage = round((int(fraction[0]) / int(fraction[1])) * 100)
            if percentage<=1:
                print("E")
            elif percentage>=99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        else:
            print("Incorrect Format")
    except (ValueError, ZeroDivisionError, IndexError):
        print("Incorrect Format")