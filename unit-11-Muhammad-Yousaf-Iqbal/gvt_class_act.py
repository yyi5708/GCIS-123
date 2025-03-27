import goatils
import random

COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
COMMON : WHITE + "C", 
UNCOMMON : LIGHT_GREEN + "U", 
RARE : BLUE + "R", 
LEGENDARY : ORANGE + "L"}

class Card:

    __slots__ = ["__name", "__cost", "__rarity", "__faction", "__attack_power", "__health"]

    def __init__(self, name, cost, rarity, faction, attack_power, health):

        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__faction = faction
        self.__attack_power = attack_power
        self.__health = health
    
    def get_name(self):

        return self.__name
    
    def get_cost(self):

        return self.__cost
    
    def get_rarity(self):

        return self.__rarity
    
    def get_faction(self):

        return self.__faction
    
    def get_attack_power(self):

        return self.__attack_power
    
    def get_health(self):

        return self.__health
    
    def __repr__(self):

        output = RARITY_STRINGS[self.__rarity] + " " + self.__name \
            + "\nRarity: " + RARITY_STRINGS[self.__rarity] \
            + "\nFaction: " + self.__faction \
            + "\nResource Cost: " + str(self.__cost) \
            + "\nHealth Points: " + str(self.__health) \
            + "\nAttack Power: " + str(self.__attack_power)
        return output
    
    def __str__(self):

        return "[" + self.__faction[0] + self.__name[0] \
            + " " + "{:02d}".format(self.__cost) \
            + " " + "{:02d}".format(self.__attack_power) \
            + " " + "{:02d}".format(self.__health) \
            + "]"
    
    def damage(self, amount):

        if amount <= self.__health:
            self.__health -= amount
            return 0
        else:
            current = self.__health
            self.__health = 0
            return amount - current
    
    def is_conscious(self):

        return self.__health > 0
    
    def __eq__(self, other):

        if type(self) == type(other):
            return self.__rarity == other.__rarity \
                and self.__faction == other.__faction \
                and self.__cost == other.__cost \
                and self.__attack_power == other.__attack_power
        else:
            return False
    
    def __lt__(self, other):

        if type(self) == type(other):
            if self.__cost == other.__cost:
                return self.__name < other.__name
            else:
                return self.__cost < other.__cost
        else:
            return False

TROLL_NAMES = ["Troll", "Trolling", "Trollzord", "Troll Jr.", "Mr. Troll", "Internet Troll", "Cave Troll", "Mountain Troll", "Rock Troll", "Fire Troll", "Yermommaza Troll", "Troller", "Loltroll"]

def make_card(faction, rarity):

    name = ""
    if faction == "Goats":
        name = goatils.make_goat_name()
    else:
        randex = random.randrange(len(TROLL_NAMES))
        name = TROLL_NAMES[randex]
    total = 0
    cost = 0
    if rarity == COMMON:
        total = 8
        cost = random.randint(1, 3)
    if rarity == UNCOMMON:
        total = 12
        cost = random.randint(2, 5)
    if rarity == RARE:
        total = 16
        cost = random.randint(4, 7)
    if rarity == LEGENDARY:
        total = 24
        cost = 10
    else:
        raise ValueError("Invalid Card Rarity: " + str(rarity))
    health = random.randint(1, total)
    attack_power = total - health
    return Card(name, cost, rarity, faction, attack_power, health)

def make_deck(faction):

    deck = []
    for i in range(20):
        deck.append(make_card(faction, COMMON))
    for i in range(10):
        deck.append(make_card(faction, UNCOMMON))
    for i in range(8):
        deck.append(make_card(faction, RARE))
    for i in range(2):
        deck.append(make_card(faction, LEGENDARY))
    random.shuffle(deck)
    return deck

def main():

    x = make_deck("Troll")
    for y in x:
        print(repr(y), "\n\n")
    y = make_card("Goats", COMMON)
    card1 = Card("Harry O'Bleater III", 5, RARE, "Goat", 0, 5)
    card2 = Card("Trollzord", 2, UNCOMMON, "Troll", 6, 4)
    print(card1.get_name())
    print(card1.get_faction())
    print(card1.get_health())
    print(card2.get_attack_power())
    print(card2.get_cost())
    print(card2.get_rarity())
    print(repr(card2))
    print(card1, card2)
    print(card1.damage(20))
    print(card1)
    print(card2.damage(2))
    print(card2)
    card3 = Card("Goaty McGoaterson", 5, RARE, "Goat", 0, 5)
    print(card1 == card3)
    print(card2 == card3)
    cards = [card1, card2, card3]
    print(cards)

if __name__ == "__main__":

    main()