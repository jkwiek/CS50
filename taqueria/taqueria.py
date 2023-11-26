entrees={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def printTotal(item):


while True:
    try:
        item = input("Item: ").title()
        printTotal(item)
        price = entrees[item]
        itemsum = 0
        itemsum += float(price)
        print("Total: $", itemsum, sep="")
    except (ValueError, KeyError):
        continue
    except EOFError:
        print()
        break


