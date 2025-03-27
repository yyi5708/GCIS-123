#Muhammad Yousaf Iqbal

from pokedox import Pokedex

def battle(party_1, party_2):

    (round_number) = (1)
    while len(party_1) > (0) and len(party_2) > (0):
        print(f"Round: {round_number}")
        print(f"Party 1: {party_1}")
        print(f"Party 2: {party_2}")
        (pokemon_1) = (party_1.pop())
        (pokemon_2) = (party_2.pop())
        if (pokemon_1) == (pokemon_2):
            print(f"{pokemon_1} and {pokemon_2} battle to a draw")
            party_1.add(pokemon_1)
            party_2.add(pokemon_2)
        else:
            (winner) = max(pokemon_1, pokemon_2)
            (loser) = (pokemon_1) if (winner) == (pokemon_2) else (pokemon_2)
            print(f"{winner} has won the round over {loser}")
            (winner_party) = (party_1) if (winner) in (party_1) else (party_2)
            (loser_party) = (party_1) if (loser) in (party_1) else (party_2)
            winner_party.add(winner)
            loser.lose_round(winner.damage_points)
            if (loser.is_fainted()):
                print(f"{loser} has fainted and is out of the battle")
            else:
                loser_party.add(loser)
        input("Press enter to continue to the next round")
        (round_number) += (1)
    if len(party_1) > (0):
        print("Winning: Party 1")
    if len(party_2) > (0):
        print("Winning: Party 2")
    else:
        return(True)

def main():

    (pokedex_1) = Pokedex()
    pokedex_1.load("data/pokemon.csv")
    (party_1, party_2) = pokedex_1.create_parties()
    battle(party_1, party_2)

if __name__ == "__main__":

    main()

#Done