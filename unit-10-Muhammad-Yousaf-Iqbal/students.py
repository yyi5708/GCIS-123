#

class Student:
    __slots__ = ["id", "name", "credits", "gpa"]

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0

def print_student(student):
    print("Student: ", student.id, student.name, student.credits, student.gpa)

def main():
    student1 = Student("123-ABC", "Farris")
    student2 = Student("456-DEF", "Sarah")
    print_student(student1)
    print_student(student2)
    
if __name__ == "__main__":
    main()