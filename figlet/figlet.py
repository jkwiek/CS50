from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit("First command-line argument is not valid, use -f or --font only")
    elif sys.argv[2] not in fonts:
        sys.exit("Second command-line argument is not a valid font")
    else:
        f = sys.argv[2]
else:
    sys.exit

figlet.setFont(font=f)
text = input("Input: ")
print("Output:",figlet.renderText(text), sep = "\n")
