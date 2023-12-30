import sys
import json
import requests
while True:
response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")

    try:
        input = float(sys.argv[1])


    except ValueError:
        print("Command-line argument is not a number")
        break
    except IndexError:
        print("Missing command-line argument")
        break
    else:
        print(conversion_factor)
#except requests.RequestException:



