def evens(n):
    sum = 0
    for even in range(0, n+1, 2):
        sum += even
    return sum

def runner(function, number):
    print("Running '", function.__name__, "'...")
    result = function(number)
    print(result)

def main():
    runner(evens , 10)
    runner(evens, 100)

main()