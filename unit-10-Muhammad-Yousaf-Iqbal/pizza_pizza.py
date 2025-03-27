#Muhammad Yousaf Iqbal

class Toppings:

    def __init__(self, name, order_code, price):

        (self.name) = (name)
        (self.order_code) = (order_code)
        (self.price) = (price)

class Pizza:

    def __init__(self):

        (self.base_cost) = (5.0)
        (self.toppings) = ({"Cheese": [], "Meats": [], "Veggies": []})
        (self.cheese_toppings) = ({
            "Fresh Mozzarella": Toppings("Fresh Mozzarella", "F", 1.0),
            "Shredded Cheese": Toppings("Shredded Cheese", "S", 0.0),
            "Cheddar": Toppings("Cheddar", "C", 0.5),
            "None": Toppings("None", "N", 0.0),
        })
        (self.meat_toppings) = ({
            "Pepperoni": Toppings("Pepperoni", "P", 1.5),
            "Sausage": Toppings("Sausage", "S", 1.5),
            "Bacon": Toppings("Bacon", "B", 1.0),
            "Meatball": Toppings("Meatball", "M", 2.0),
            "None": Toppings("None", "N", 0.0),
        })
        (self.veggie_toppings) = ({
            "Mushrooms": Toppings("Mushrooms", "M", 1.0),
            "Bell Peppers": Toppings("Bell Peppers", "B", 1.0),
            "Jalapeno Peppers": Toppings("Jalapeno Peppers", "J", 1.0),
            "Pineapple": Toppings("Pineapple", "P", 1.5),
            "None": Toppings("None", "N", 0.0),
        })
    
    def add_topping(self, toppings, category):

        (toppings) = Toppings()
        (self.toppings[category].append(toppings))
    
    def get_total_cost(self):

        (total_cost) = (self.base_cost)
        for (category) in (self.toppings):
            for (topping) in (category):
                (total_cost) += (topping.price)
        return(total_cost)
    
    def get_cheese_topping(self, name):

        return(self.cheese_toppings[name])
    
    def get_meat_topping(self, name):

        return(self.meat_toppings[name])
    
    def get_veggie_topping(self, name):

        return(self.veggie_toppings[name])

def print_toppings(category, toppings):

    (toppings) = Pizza()
    print(f"{category} Toppings:")
    if (category) == ("Cheese"):
        (topping_dict) = (toppings.cheese_toppings)
    if (category) == ("Meat"):
        (topping_dict) = (toppings.meat_toppings)
    if (category) == ("Veggie"):
        (topping_dict) = (toppings.veggie_toppings)
    else:
        print("Error.")
    for (topping) in (topping_dict):
        print(f"{topping.name} ({topping.order_code}): ${topping.price}")
        
def order_pizza(toppings):

    (toppings) = Pizza()
    print_toppings("Cheese", toppings)
    (cheese) = input("Enter your cheese toppings: ")
    (cheese_toppings) = [toppings.get_cheese_topping(cheese)]
    print_toppings("Meat", toppings)
    (meat) = input("Enter your meat toppings: ")
    (meat_toppings) = [toppings.get_meat_topping(meat)]
    print_toppings("Veggie", toppings)
    (veggie) = input("Enter your veggie toppings: ")
    (veggie_toppings) = [toppings.get_veggie_topping(veggie)]
    (total_cost) = (5.0)
    (toppings_list) = (cheese_toppings) + (meat_toppings) + (veggie_toppings)
    for (topping) in (toppings_list):
        (total_cost) += (topping.price)
    (pizza) = Pizza(total_cost, cheese_toppings, meat_toppings, veggie_toppings)
    return(pizza)

def print_pizza(pizza):

    (pizza) = Pizza()
    print("Pizza toppings:")
    for (category), (toppings) in (pizza.toppings):
        print(f"{category} Toppings:")
        if (toppings):
            for (toppings) in (toppings):
                print(f"{toppings.name} ({toppings.order_code}): ${toppings.price}")
        else:
            print("Error.")
    print(f"Total cost: ${pizza.price}")

def main():

    #print("Welcome to the pizza factory!")
    #(toppings) = Pizza()
    #print("First pizza: ")
    #pizza_1 = order_pizza(toppings)
    #print_pizza(pizza_1)
    #print("Second pizza: ")
    #pizza_2 = order_pizza(toppings)
    #print_pizza(pizza_2)
    #total_cost = pizza_1.price + pizza_2.price
    #print(f"Total cost for both pizzas: ${total_cost:}")
    return()

if __name__ == "__main__":

    main()

#Done