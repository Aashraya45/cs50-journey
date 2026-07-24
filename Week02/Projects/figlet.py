import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

def print_figlet(font_name):
    text = input("Input: ")
    figlet.setFont(font=font_name)
    print(figlet.renderText(text))

if len(sys.argv) == 1:
    print_figlet(random.choice(fonts))

elif len(sys.argv) == 3:
    flag = sys.argv[1]
    font_name = sys.argv[2]
    
    if flag in ["-f", "--font"] and font_name in fonts:
        print_figlet(font_name)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
