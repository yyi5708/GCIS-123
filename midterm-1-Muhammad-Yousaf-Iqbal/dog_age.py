def human_years(dog_years):
    
    if dog_years <= 0:
        return (None)
    if dog_years == 1:
        return (15)
    if dog_years == 2:
        return (24)
    else:
        return (24 + (dog_years * 5) - 10)

def main():

    zero = human_years(0)
    print("Dog years in human years is: ",zero)
    two = human_years(2)
    print("Dog years in human years is: ",two)
    four = human_years(4)
    print("Dog years in human years is: ",four)
    six = human_years(6)
    print("Dog years in human years is: ",six)
    eight = human_years(8)
    print("Dog years in human years is: ",eight)
    ten = human_years(10)
    print("Dog years in human years is: ",ten)

main()

#DONE.