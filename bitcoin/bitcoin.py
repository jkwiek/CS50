import sys
import json
import requests

response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
response = response.json()
conversion_factor = response["bpi"]
conversion_factor = conversion_factor["USD"]
conversion_factor = conversion_factor["rate_float"]


n = sys.argv[1]

if not n.replace(".", "", 1).isdigit():
    print("Command-line argument is not a number")
    sys.exit
elif len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit
else:
    cost = float(n) * conversion_factor
    print(f"${cost:,.4f}")

#except requests.RequestException:

#BPI->USD->rate_float


