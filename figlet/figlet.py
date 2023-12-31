import pyfiglet
import sys
import random

fonts = [pyfiglet.figlet]

if len(sys.argv) == 1:
    font = random.choice(fonts)
    raw_text = input("Input: ")
    figlet_text = pyfiglet(raw_text)
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or "--font" or sys.argv[2] not in fonts:
        sys.exit
else:
    sys.exit
