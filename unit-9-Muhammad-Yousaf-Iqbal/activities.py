import arrays

def find_maximum(dictionary):
    max_key = None
    max_value = 0
    for key in dictionary:
        value = dictionary[key]
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

def hashes():
    x = hash("Hello World!")
    y = hash("Hellow world!")
    print(x)
    print(y)
    x_1 = hash("A"*100000)
    x_2 = hash("A"*10000000000)
    print(x_1)
    print(x_2)

def collisions(filename, length, hash_function=hash()):
    an_array = arrays.Array(length, None)
    with open(filename) as file:
        count = 0
        for line in file:
            line = line.strip()
            if line == "":
                continue
            hash_code = hash_function(line)
            index = hash_code % length
            if an_array[index] is None:
                an_array[index] = line
                count += 1
            else:
                return count

def ascii_codes(a_string):
    for (char) in (a_string):
        print(char, ":", ord(char), sep="")

def main():
    #dictionary = {"one":1, "two":200, "three":3}
    #print(find_maximum(dictionary))
    #hashes()
    #hashes()
    #print(collisions("data/alice.txt", 100, hash()))
    string = "GCIS-123"
    print(ascii_codes(string))
    return

main()