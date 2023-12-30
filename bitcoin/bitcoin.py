import sys
import json
import requests

response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()
conversion_factor = response({"bpi"["rate_float"]})


n = float(sys.argv[1])

if ValueError:
    print("Command-line argument is not a number")
    sys.exit
elif IndexError:
    print("Missing command-line argument")
    sys.exit

cost = n * conversion_factor
print(f"{cost:,.4f}")
#except requests.RequestException:



