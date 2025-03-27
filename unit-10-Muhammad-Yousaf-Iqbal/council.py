#Muhammad Yousaf Iqbal

class Council:

    __slots__ = ["Administrators" , "Chief_Administrator"]

    def __init__(Self , Administrators , Chief_Administrator):

        Self.Administrators = Administrators
        Self.Chief_Administrator = Chief_Administrator

class Chief_Administrator_Biography:

    __slots__ = ["Name" , "Region" , "Departments" , "Languages"]

    def __init__(Self , Name , Region , Departments , Languages):

        Self.Name = Name
        Self.Region = Region
        Self.Departments = Departments
        Self.Languages = Languages

class Administrators_Biographies:

    __slots__ = ["Name" , "Region" , "Departments" , "Languages"]

    def __init__(Self , Name , Region , Departments , Languages):

        Self.Name = Name
        Self.Region = Region
        Self.Departments = Departments
        Self.Languages = Languages

def main():

    print("\n")
    council_print = Council("Nasqu Baankai and Ittail Xaqe and Drincaet Drephral and Thrilgiens Vraurcaels." , "Gregzuth Yehrins.")
    print("Council: ")
    print("     Chief Administrator: " , council_print.Chief_Administrator)
    print("     Administrators: " , council_print.Administrators)
    print("\n")
    chief_administrator_biography_print = Chief_Administrator_Biography("Gregzuth Yehrins." , "Aalxo." , "Resource Management." , "Meinmese and Geulmese.")
    print("Chief Administrator Biography: ")
    print("     Name: " , chief_administrator_biography_print.Name)
    print("     Region: " , chief_administrator_biography_print.Region)
    print("     Departments: " , chief_administrator_biography_print.Departments)
    print("     Languages: " , chief_administrator_biography_print.Languages)
    print("\n")
    administrators_biographies_print_1 = Administrators_Biographies("Nasqu Baankai." , "Stakins." , "Interplanetary Affairs and Defense." , "Meinmese and Vietina.")
    administrators_biographies_print_2 = Administrators_Biographies("Ittail Xaqe." , "Bhuhleks." , "Finance and Transportation and Health Services." , "Meinmese and Geulmese.")
    administrators_biographies_print_3 = Administrators_Biographies("Drincaet Drephral." , "Teehors." , "Planetary Affairs and Agriculture." , "Meinmese and Ulbiya.")
    administrators_biographies_print_4 = Administrators_Biographies("Thrilgiens Vraurcaels." , "Stadu." , "Education and Justice and Food Management." , "Tezniekani and Meinmese.")
    print("Administrators Biographies: ")
    print("     Name: " , administrators_biographies_print_1.Name)
    print("     Region: " , administrators_biographies_print_1.Region)
    print("     Departments: " , administrators_biographies_print_1.Departments)
    print("     Languages: " , administrators_biographies_print_1.Languages)
    print("\n")
    print("     Name: " , administrators_biographies_print_2.Name)
    print("     Region: " , administrators_biographies_print_2.Region)
    print("     Departments: " , administrators_biographies_print_2.Departments)
    print("     Languages: " , administrators_biographies_print_2.Languages)    
    print("\n")
    print("     Name: " , administrators_biographies_print_3.Name)
    print("     Region: " , administrators_biographies_print_3.Region)
    print("     Departments: " , administrators_biographies_print_3.Departments)
    print("     Languages: " , administrators_biographies_print_3.Languages)   
    print("\n")
    print("     Name: " , administrators_biographies_print_4.Name)
    print("     Region: " , administrators_biographies_print_4.Region)
    print("     Departments: " , administrators_biographies_print_4.Departments)
    print("     Languages: " , administrators_biographies_print_4.Languages)
    print("\n")

if __name__ == "__main__":

    main()

#End