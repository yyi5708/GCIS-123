#MYI

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

class Player:

    __slots__ = ["__name" , "__score" , "__resource_points" , "__deck" , "__hand" , "__battalion" , "__discarded"]

    def __init__(self, name, deck):

        self.__name = name
        self.__score = 20
        self.__resource_points = 0
        self.__deck = deck
        self.__hand = []
        self.__battalion = []
        self.__discarded = []
    
    def get_name(self):

        return self.__name
    
    def get_score(self):

        return self.__score

    def get_resource_points(self):

        return self.__resource_points

    def get_deck(self):

        return self.__deck

    def get_hand(self):

        return self.__hand

    def get_battalion(self):

        return self.__battalion

    def get_discarded(self):

        return self.__discarded
    
    def __str__(self):

        return "Player: " + str(self.__name)
    
    def __repr__(self):

        return "\nPlayer: " + str(self.__name) + "\nScore: " + str(self.__score) + "\nResource Points: " + str(self.__score) + "\nDeck: " + str(self.__deck) + "\nDiscarded: " + str(self.__discarded) + "\nBattalion: " + str(self.__battalion) + "\nHand: " + str(self.__hand) + "\n"

    def start_turn(self):
    
        self.__resource_points = min(self.__resource_points + 1, 10)
        card = self.__deck.draw()
        self.__hand.append(card)

    def play_card(self, index):

        card = self.__hand[index - 1]
        self.__resource_points -= card.get_resource_points()
        self.__battalion.append(card)
        self.__hand.pop(index - 1)

    def get_damage(self):

        damage = 0
        for card in self.__battalion:
            damage += card.get_battalion()
        return damage
    
    def defeat(self, player):
    
        if player.get_resource_points() <= 0 or len(player.get_deck()) == 0 and len(player.get_hand()) == 0:
            return True
        else:
            return False

#Done