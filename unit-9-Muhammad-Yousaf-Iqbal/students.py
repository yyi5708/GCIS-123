def make_student(id, name):
    return [id, name, 0, 0]

def add_student(population, id, name):
    for index in range(len(population)):
        student = population[index]
        if student[0] == id:
            population.pop(index)
            break
        new_student = make_student(id, name)
        population += [new_student]

def get_student(population, id):
    for student in population:
        if student[0] == id:
            return student
    return None

def add_credits(population, id, credits):
    student = get_student(population, id)
    if student is not None:
        student[2] += credits
        
def get_credits(population, id):
    student = get_student(population, id)
    if student is not None:
        return student[2]
    else:
        return None

def main():
    population = {}
    add_student(population, "01", "Bob")
    add_student(population, "02", "Gary")
    add_student(population, "03", "Gavin")
    add_student(population, "04", "Billy")
    print(population)
    print()
    x = get_student(population, "01")
    print(x)
    print(get_student(population, "not_real"))
    add_credits(population, "01", 4)
    print(x)
    print(get_credits(population, "01"))

main()