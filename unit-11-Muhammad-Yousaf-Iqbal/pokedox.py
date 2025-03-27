#Muhammad Yousaf Iqbal

import csv
import random
from pokemon import Pokemon

class Pokedex:

    (__slots__) = (["__pokemon_list"])

    def __init__(self):
    
        (self.__pokemon_list) = ([])

    def load(self, filename):
    
        with open(filename) as (file):
            (reader) = csv.reader(file)
            for (record) in (reader):
                (name, type, health_points, damage_points) = (record)
                (pokemon) = Pokemon(name, type, health_points, damage_points)
                self.__pokemon_list.append(pokemon)
            else:
                return(True)

    def create_parties(self):
    
        (party_1) = set()
        (party_2) = set()
        random.shuffle(self.__pokemon_list)
        while len(party_1) < (6) or len(party_2) < (6):
            for (pokemon) in (self.__pokemon_list):
                if len(party_1) < (6) and (pokemon) not in (party_1):
                    party_1.add(pokemon)
                if len(party_2) < (6) and (pokemon) not in (party_2):
                    party_2.add(pokemon)
                if len(party_1) == (6) and len(party_2) == (6):
                    return(party_1, party_2)
                else:
                    return(True)
                    
def main():

    pass

if __name__ == "__main__":

    main()

#Done