def numbers():
    numbers = range(0, 101)
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

print(numbers())