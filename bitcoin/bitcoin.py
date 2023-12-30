import sys
import requests
while True:
    try:
        input = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        break

#except requests.RequestException:



