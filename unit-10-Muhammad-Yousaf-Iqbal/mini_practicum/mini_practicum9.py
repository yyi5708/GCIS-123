#Muhammad Yousaf Iqbal

def make_letter_frequency(filename):

    (count) = ({})
    with open(filename) as (file):
        for (line) in (file):
            (line) = line.lower()
            (line) = line.strip()
            for (char) in (line):
                if ("a") <= (char) <= ("z"):
                    if (char) in (count):
                        count[char] += (1)
                    else:
                        count[char] = (1)
    return (count)

def print_letter_frequency(dictionary):

    (sort) = sorted(dictionary)
    for (letter) in (sort):
        if (letter) in (dictionary):
            (count) = dictionary[letter]
            print(f"{letter}: {count}.")
    (pop_letter) = (None)
    (pop_count) = (0)
    for (letter) in (sort):
        if (letter) in (dictionary):
            (count) = dictionary[letter]
            if (count) > (pop_count):
                (pop_letter) = (letter)
                (pop_count) = (count)
    print(f"the most popular letter: {pop_letter}: {pop_count}.")

def main():

    filename_1 = "data/rit_mission.txt"
    filename_2 = "data/alice.txt"
    print(make_letter_frequency(filename_1))
    print("\n")
    print(make_letter_frequency(filename_2))
    print("\n")
    one = make_letter_frequency(filename_1)
    print_letter_frequency(one)
    print("\n")
    two = make_letter_frequency(filename_2)
    print_letter_frequency(two)

if __name__ == "__main__":

    main()

#Done