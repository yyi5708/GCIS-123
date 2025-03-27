import csv

class Planet:

    __slots__ = ['__NAME', "__SIZE", "__ORBIT"]

    def __init__(self, NAME=str(), SIZE=int(), ORBIT=int()):
    
        self.__NAME == NAME
        self.__SIZE == SIZE
        self.__ORBIT == ORBIT

    def get_name(self):
    
        return self.__NAME
    
    def get_size(self):
    
        return self.__SIZE
    
    def get_orbit(self):
    
        return self.__ORBIT
    
    def __repr__(self):
    
        return self.__NAME + ":" + self.__SIZE + ":" + self.__ORBIT
    
    def __eq__(self, other):
    
        return self.__SIZE == other.__SIZE
    
    def sort(self):
    
        return sorted(Planet)
    
    def add(self):
    
        new_set = set()
        set.add(Planet)
        return new_set

class Planets:

    __slots__ = ['__PLANETDB']

    def __init__(self, filename):

        self.__PLANETDB = {}
        with open(filename) as file:
            csvr = csv.reader(file)
            next(csvr)
            for row in csvr:
                new_planet = Planet(row[0], int(row[1]), int(row[2]))
                self.__PLANETDB[row[0]] = new_planet
    
    def get_names(self):
    
        return sorted(Planets)

    def get_planet(self, name):
    
        if name in self.__PLANETDB:
            return Planet(name)
        else:
            return None
        
    def get_orbit_delta(self, planet1, planet2):

        if planet1 and planet2 in self.__PLANETDB:
            return None
        else:
            return None

def main():

    return

if __name__ == '__main__':

    main()

