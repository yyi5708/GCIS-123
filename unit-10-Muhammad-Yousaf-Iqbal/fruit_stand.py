#

class Fruit:
    type = ("No Type")
    price = (0.0)

apples = Fruit()
apples.type = ("Apples")
apples.price = ("1.00")

oranges = Fruit()
oranges.type = ("Oranges")
oranges.price = ("1.50")

watermelons = Fruit()
watermelons.type = ("Watermelons")
watermelons.price = ("2.00")

def total_price(basket):
    total = 0
    for fruit in basket:
        total+= Fruit.price
    return total

def count_fruit(basket):
    count = {}
    for type in basket:
        type = Fruit.type
        if type in count:
            number = count[type]
            number += 1
            count[type] = number
        else:
            count[type] = 1   

def main():
    basket = []
    while True:
        type = input("fruit >> ")
        if type == "":
            break
        elif type == "apple":
            basket.append("APPLE")
        elif type == "orange":
            basket.append("ORANGE")
        elif type == "watermelon":
            basket.append("WATERMELON")
        else:
            print("no such fruit, try again.")

    count = count_fruit(basket)
    for type in count:
        number = count[type]
        print(type, number)

    print("amount due: ", total_price(basket))

if __name__ == "__main__":
    main()