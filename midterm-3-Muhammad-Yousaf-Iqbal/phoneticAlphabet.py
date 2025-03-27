"""
Complete the function below to translate the letters of a given string into a
list of code words for each letter.
You have been provided a Phonetic Alphabet dicitionary with uppercase letters
as keys and code words as values.
The given string may contain any character, including lowercase letters which
should be translated to uppercase letters.  If a character does not exist as a
dictionary key, it should be skipped.
Examples:
    translate("Niner")   # returns ['November', 'India', 'November', 'Echo', 'Romeo']
    translate("S-O-S")   # returns ['Sierra', 'Oscar', 'Sierra']
    translate("Top Gun") # returns ['Tango', 'Oscar', 'Papa', 'Golf', 'Uniform', 'November']
    translate("python")  # returns ['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
"""
# Do not change dictionary
PHONETIC_ALPHABET = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta",
                     "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel",
                     "I":"India", "J":"Juliett", "K":"Kilo", "L":"Lima",
                     "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa",
                     "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango",
                     "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"X-ray",
                     "Y":"Yankee", "Z":"Zulu"}
def translate(a_string):
    for char in a_string:
        if char in PHONETIC_ALPHABET:
            x = []
            char = PHONETIC_ALPHABET(key="")
            x.append(char)
            return x
        if char.upper() in PHONETIC_ALPHABET:
            x = []
            char = PHONETIC_ALPHABET(key="")
            x.append(char)
            return x
        else:
            pass
# For manual testing purposes, you may change as needed
def main():
    print(translate("S-O-S"))
    print(translate("python"))
    #print(translate_alt("python"))
if __name__ == "__main__":
    main()
#MYI
