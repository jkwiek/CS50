from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or "--font":
        sys.exit(")
    elif sys.argv[2] not in fonts:
        sys.exit("Second command-line argument is not  invalid font")
    else:
        f = sys.argv[2]
else:
    sys.exit

figlet.setFont(font=f)
text = input("Input: ")
print("Output:",figlet.renderText(text), sep = "\n")
