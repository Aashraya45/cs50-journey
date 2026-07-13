Match statements might work better than if in some cases 
for example:
name = input("What is your name?")
if name == "Harry" or name = "Hermione" or name = "Ron":
    print("Gryffindor)
elif name =="Draco":
    print("Slytherin")
else:
    print("Who?")

Instead of this you could write :
name = input("What is your name?")
match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")  
    case _:     #here _ means anything else
        print("Who?")

in order to reuse a function in any other python program, make the main function then at the end
if __name__=="__main__":
   main()
    

