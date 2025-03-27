#

class MajicCard:

    __slots__ = ["name", "mana_value", "power", "toughness"]

    def __init__(self, name, mana_value, power, toughness):

        self.name = name
        self.mana_value = mana_value
        self.power = power
        self.toughness = toughness

def main():

    card = MajicCard("Wood Elves", 3, 1, 1)
    #card.name = "Wood Elves"
    print(card.name)
    print(card.mana_value)
    print(card.power)
    print(card.toughness)

main()