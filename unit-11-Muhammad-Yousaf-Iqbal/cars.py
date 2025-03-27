class Car:

    __slots__ = ["__VIN", "__MAKE", "__MODEL", "__YEAR", "__MILEAGE", "__FUEL"]

    def __init__(self, VIN, MAKE, MODEL, YEAR, MILEAGE=0, FUEL=0):
    
        self.__VIN = VIN
        self.__MAKE = MAKE
        self.__MODEL = MODEL
        self.__YEAR = YEAR
        self.__MILEAGE = 0
        self.__FUEL = 0

    def get_vin(self):
    
        return self.__VIN

    def get_make(self):
    
        return self.__MAKE

    def get_model(self):
    
        return self.__MODEL
    
    def get_year(self):
    
        return self.__YEAR

    def get_mileage(self):
    
        return self.__MILEAGE

    def get_fuel(self):
    
        return self.__FUEL
    
    def print_car(Car):
    
        car_1 = Car("123456789", "TOYOTA", "CAMRY", "2022")
        print("VIN: ", car_1.__VIN)
        print("MAKE: ", car_1.__MAKE)
        print("MODEL: ", car_1.__MODEL)
        print("YEAR: ", car_1.__YEAR)
        print("MILEAGE: ", car_1.__MILEAGE)
        print("FUEL: ", car_1.__FUEL)

def main():

    pass

main()