def main():
    time = input("What time is it? ")
    x = convert(time)
    if x>=7 and x<=8:
        print("breakfast time")
    elif x>=12 and x<=13:
        print("lunch time")
    elif x>=18 and x<=19:
        print("dinner time")

def convert(x):
    y=x.split(":")
    return (float(y[0])+float(y[1])/60)

if __name__ == "__main__":
    main()
    