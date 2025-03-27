#Muhammad Yousaf Iqbal

import time

def hash_first_char(string):

    if (string) == (""):
        return (0)
    else:
        return ord(string[0])

def hash_sum(string):

    (sum) = (0)
    for (char) in (string):
        (sum) += ord(char)
    return (sum)

def hash_positional_sum(string):

    (sum) = (0)
    (power) = (1)
    for (i) in range(len(string)):
        (sum) += ord(string[i]) * (power)
        (power) *= (31)
    return (sum)

def build_collision_counter(hash_function):

    (collision_count) = ({})
    with open("data/long_line_words.txt") as (file):
        for (line) in (file):
            (hashed_line) = hash_function(line.strip())
            if (hashed_line) in (collision_count):
                (collision_count[hashed_line]) += (1)
            else:
                (collision_count[hashed_line]) = (1)
    return (collision_count)

def hash_test(collision_counter, hash_function):

    (hash_name) = (hash_function.__name__)
    (input) = sum(collision_counter.values())
    (collisions) = sum([count - 1 for count in collision_counter.values()])
    (total_collision_rate) = round(collisions / input, 2) * (100)
    (maximum_collisions) = max(collision_counter.values()) - (1)
    (output) = len(collision_counter)
    (spread) = round(output / input, 2) * (100)

    def timer():
    
        (start) = time.perf_counter()
        with open("data/long_line_words.txt") as (file):
            for (line) in (file):
                hash_function(line.strip())
        (end) = time.perf_counter()
        return (end - start)

    (speed) = round(timer(), 2)
    print("\n")
    print("hash function: ", hash_name)
    print("total collision rate: ", total_collision_rate, "%")
    print("maximum collisions: ", maximum_collisions)
    print("spread: ", spread, "%")
    print("speed: ", speed, "seconds")
    print("\n")

def main():

    print("hash_first_char function: ")
    print(hash_first_char("joe"))
    print(hash_first_char("mama"))
    print("hash_sum function: ")
    print(hash_sum("joe"))
    print(hash_sum("mama"))
    print("hash_positional_sum function: ")
    print(hash_positional_sum("joe"))
    print(hash_positional_sum("mama"))
    (hash_functions) = ([hash, hash_first_char, hash_sum, hash_positional_sum])
    for (hash_function) in (hash_functions):
        (collision_counter) = build_collision_counter(hash_function)
        hash_test(collision_counter, hash_function)
    pass

if __name__ == "__main__":
    main()

#Done