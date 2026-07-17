Errors:
1) Syntax Error: Problem pinpointed in the terminal, just read it out and fix it
2)  Runtime Errors:  Occurs when an operation is applied to an incompatible data type (e.g., adding a string to an integer)
  eg, int("Cat")  
  This specifically is a Value Error. ValueError: Raised when a function gets an argument of the right type but an inappropriate value.
To fix value errorrs:

try:
    x= int(input("What's x? ))
    print(f"x is {x}")
except ValueError:
    print("Please enter a number")

# SO now if the user who has maybe got mallicious intent , when they enter something like cat instead of an integer,
they'll have to face the messege "Please enter a number"

So, you can just ask python to detect any type of error by just substituting the Value Error in the code with Error but what that'll do is they'll disguise your systematic errrors like the syntax error which might make you feel like the code's working just fine when python's just hiding your problems.

So, this is not quite the best practice as it'd be optimal to have only the line of code which might see error inside the try block so the better code would be:
try:
    x= int(input("What's x? ))
except ValueError:
    print("Please enter a number")
else:
    print(f"x is {x}")
#So, this means we first try to take input and incase that the Value error doesn't happen, the else statement occurs, here except is like if

#Instead of printing "Please enter a number" you could just write pass and it would ignore invalid input


#When you're reading this please check the projects out cause these were by far the hardest and rewarding in the sense that they taught so many new things
