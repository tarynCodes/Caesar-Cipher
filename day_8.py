# functions with parameters
import math


# positional arguments
def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}?")

greet_with("Taryn", "Darwen")

# keyword arguments
greet_with(location="dundee", name="Taryn")


# Paint calc
def paint_calc(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall (m)"))
test_w = int(input("Width of wall (m)"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)


