#MYI

import gvt

def print_players(player, opponent):

    print(repr(opponent))
    print()
    print(repr(player))

def take_turn(player, opponent):

    player.start_turn()
    print_players(player, opponent)
    while True:
        command = input(str(player) + ">>")
        tokens = command.split()
        if tokens[0].upper() == "Q":
            break
        if tokens[0].upper() == "H":
            index = int(tokens[1]) - 1
            print(player.hand[index])
        if tokens[0].upper() == "B":
            index = int(tokens[1]) - 1
            print(player.battalion[index])
        if tokens[0].upper() == "E":
            index = int(tokens[1]) - 1
            print(opponent.battalion[index])
        if tokens[0].upper() == "P":
            index = int(tokens[1]) - 1
            x = player.play_card(index)
            if x:
                print_players(player, opponent)
            else:
                print("Invalid command")
        if tokens[0].upper() == "I":
            print("Available commands:")
            print("H - show a detailed string for the specified card in the player's hand")
            print("B - show a detailed string for the specified card in the player's battalion")
            print("E - show a detailed string for the specified card in the enemy player's battalion")
            print("P - play the card from the player's hand")
            print("Q - end the player's turn")
            print("I - display a list of available commands")
        else:
            print("Invalid command")
    player.attack(opponent)
    if opponent.defeat():
        print(str(opponent) + " has been defeated")
    else:
        take_turn(opponent, player)

def main():

    p1_name = input("Enter player 1 name: ")
    player1 = gvt.Player(p1_name, gvt.make_deck(gvt.GOATS))
    p2_name = input("Enter player 2 name: ")
    player2 = gvt.Player(p2_name, gvt.make_deck(gvt.TROLLS))
    player = player1
    opponent = player2
    take_turn(player, opponent)
    player, opponent = opponent, player

if __name__ == "__main__":

    main()

#Done