from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = [figlet.getFonts]

if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font = f)
    raw_text = input("Input: ")
    figlet_text = pyfiglet(raw_text)
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or "--font" or sys.argv[2] not in fonts:
        sys.exit
else:
    sys.exit
