GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

QUALITY_POINTS = {
    GRADES[0]: 4.0,
    GRADES[1]: 3.67,
    GRADES[2]: 3.33,
    GRADES[3]: 3.0,
    GRADES[4]: 2.67,
    GRADES[5]: 2.33,
    GRADES[6]: 2.0,
    GRADES[7]: 1.67,
    GRADES[8]: 1.0,
    GRADES[9]: 0,
    GRADES[10]: 0
                }

class Student:

    __slots__ = ["__id", "__name", "__credits", "__gpa"]

    def __init__(self, id, name):
    
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0

    def get_id(self):
    
        return self.__id

    def get_name(self):
    
        return self.__name

    def get_credits(self):
    
        return self.__credits

    def get_gpa(self):
    
        return self.__gpa

def print_student(student):

    print("Student: ID=", student.id, ", name=", student.name, 
        ", credits=", student.credits, ", GPA=", student.gpa, sep="")
    
class Course:

    __slots__ = ["__name", "__credits", "__grade"]

    def __init__(self, name, credits, grade):
    
        self.__name = name
        self.__credits = credits
        self.__grade = grade

def main():

    you = Student("01" , "Yousaf")
    print("ID: " , you.__id)
    print("Name: " , you.__name)
    print("Credits: " , you.__credits)
    print("GPA: " , you.__gpa)
    one = Course("GCIS-123", "4", "75%")
    print("Course Name: ", one.__name)
    print("Credits: ", one.__credits)
    print("Grade: ", one.__grade)
    two = Course("PHIL-101", "4", "100%")
    print("Course Name: ", two.__name)
    print("Credits: ", two.__credits)
    print("Grade: ", two.__grade)
    pass

main()