#MYI

import csv
import random

class Task:

    __slots__ = ["__name", "__location"]

    def __init__(self, name: str(), location: str()):
    
        self.__name = name
        self.__location = location
    
    def get_name(self):
    
        return self.__name
    
    def get_location(self):
    
        return self.__location
    
    def __str__(self):

        return self.__name + "in" + self.__location

def file(filename):

    tasks = []
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name, location = row
            tasks.append(name, location)
    return tasks

class Crewmate:

    __slots__ = ["__color", "__tasks", "__murdered"]
    
    def __init__(self, color: str()):
    
        self.__color = color
        self.__tasks = []
        self.__murdered = False
    
    def get_color(self):

        return self.__color
    
    def get_tasks(self):

        return self.__tasks
    
    def get_murdered(self):

        return self.__murdered
    
    def add_task(self, task):

        task = Task()
        self.__tasks.append(task)
    
    def murder(self):
        self.__murdered = True
    
    def __str__(self):
    
        if self.__murdered:
            return self.__color + "Crewmate (deceased)"
        else:
            return self.__color + "Crewmate"

    def __repr__(self):
        
        return "Crewmate:" + "Color:" + self.__color + "Murdered:" + self.__murdered + "Tasks:" + self.__tasks

class Ship:

    __slots__ = ["__tasks", "__locations"]
    
    def __init__(self, tasks: list(Task), locations: set()):
    
        self.__tasks = tasks
        self.__locations = locations

    def get_tasks(self):

        return self.__tasks
    
    def get_locations(self):

        return self.__locations
    
    def journey(self, imposters):

        if imposters < 1 or imposters > 4:
            raise ValueError
        crew_colors = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White", "Yellow"]
        random.shuffle(crew_colors)
        crew = []
        Crewmate = crew()
        for i in range(10):
            color = crew_colors.pop()
            tasks = self.__tasks(random.randint(3, 6))
            crew.append(Crewmate(color, tasks))
        game = [crewmate for crewmate in crew]
        murdered = []
        if self.__tasks:
            print("The imposter(s) wipe out the crew")
        else:
            print("All tasks are completed by any surviving crewmates")
        print("Surviving crew:")
        for crewmate in game:
            print(crewmate)
        print("Murdered crew:")
        for crewmate in murdered:
            print(crewmate)
        return

def main():
    
    tasks = file("tasks_01.csv")
    ship = Ship(tasks)
    while True:
        imposters = input("Enter a number of imposters:")
        if imposters == "":
            break
        if imposters < 1 or imposters > 4:
            print("Error")
        else:
            ship.journey(imposters)
    return

if __name__ == "__main__":

    main()

#Done