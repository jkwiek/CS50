import sys
import json
import requests

response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()
conversion_factor = response[]

while True:
    try:
        input = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        break
    except IndexError:
        print("Missing command-line argument")
        break
input
#except requests.RequestException:



