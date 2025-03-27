#Muhammad Yousaf Iqbal

class Pokemon:

    (__slots__) = (["__name", "__type", "__health_points", "__damage_points"])

    def __init__(self, name, type, health_points, damage_points):
    
        (self.__name) = (name)
        (self.__type) = (type)
        (self.__health_points) = (health_points)
        (self.__damage_points) = (damage_points)

    def get_damage_points(self):
    
        return(self.__damage_points)

    def lose_round(self, damage_points):
    
        (self.__health_points) -= (damage_points)

    def is_fainted(self):
    
        return(self.__health_points <= 0)

    def __str__(self):
    
        return(self.__name)

    def __repr__(self):
    
        return(f"{self.__name}:{self.__type}:{self.__health_points}")

    def __eq__(self, other):
    
        return(self.__type == other.__type and self.__health_points == other.__health_points)

    def __lt__(self, other):
    
        if (self.__type) == (other.__type):
            return(self.__health_points < other.__health_points)
        if (self.__type) == ("Water") and (other.__type) == ("Fire"):
            return(False)
        if (self.__type) == ("Fire") and (other.__type) == ("Grass"):
            return(False)
        if (self.__type) == ("Grass") and (other.__type) == ("Water"):
            return(False)
        else:
            return(True)

    def __hash__(self):
    
        return(hash((self.__name, self.__type, self.__health_points, self.__damage_points)))

def main():

    pass

if __name__ == "__main__":

    main()

#Done