expression= input("Expression:").strip()
x,y,z = expression.split(" ")
if y=="/" and z=="0":
    print("invalid expression")
if y=="/":
    print(f"{float(x)/float(z)}")
elif y=="*":
    print(f"{float(x)*float(z)}")
elif y=="+":
    print(f"{float(x)+float(z)}")
elif y=="-":
    print(f"{float(x)-float(z)}")
else:
    print("invalid")