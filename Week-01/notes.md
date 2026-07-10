# Week 1 Notes

Today I started CS50P.

Goals this week:

- Finish Lecture 0
- Finish Problem Set 0
- Build one extra project

name = name.strip()
This removes spaces from the string in the variable , eg "     Aashraya    " becomes "Aashraya"
name = name.capitalize()
This capitalizes the users name, eg"aashraya adhikari" = "Aashraya adhiakri"
name = name.title()
This capitalizes both the users name and last name, returning "Aashraya Adhikari"

You can combine these as well, eg
name = input("What is your name?").strip().title()


first, last = name.split(" ")
This will split the name from the part where the space occurst and store the part in the left side of space first followed by the one in the right side

x= input("Enter a number")
z=int(x) #Converts this to a integer
#Using float() allows decimal numbers aswell

If you want to round the float obtained to the nearest integer 
just use the round() function to do so
If you want more digits use round(variable, 2) for 2 digits and so on

or , 
for the same problem
print(f"variable: .2f") prints till 2 decimal places


Defining a function:
def Hello(name):
   print(f"Hello, {name}")
inpu= input("Enter your name")
Hello(inpu) #this runs the function

if the user does not put any input, you can set default value for the function, eg:
def Hello(name = "world")
     print(f"Hello, {name}")
Hello()
#This will print out hello world cause default value of name is world

So , the next problem we encountered was that when writing a code, the function should've always been defined at the top which is not viable as you might have to create new functions while writing.To fix this:
def main():
   All of the code assuming the function hello exists
def Hello(name):
   print(f"Hello, {name}")
main()
# Here we first defined the entire code as a function then we defined the hello funcion so that both of them coexist before we even start running any code, then we called our main code

This helps us understand scope, the variables inside any function are limited to that function itself and it cannot be used in any other function or other parts of the code


Returning values:
def main():
    x=input("Enter a number")
    print(f"x squared is {square(x)})
def square(n):
    return n*n  #This saves the value n*n 
main()

