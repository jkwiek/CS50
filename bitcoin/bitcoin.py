import sys
import requests
while True:
    try:
        input = float(sys.argv[1])
        requests.get
    except ValueError:
        print("Command-line argument is not a number")
        break
    except IndexError:
        print("Missing command-line argument")
        break
#except requests.RequestException:



