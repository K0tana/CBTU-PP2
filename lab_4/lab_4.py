from loguru import logger
import json
logger.add("debug/debug.log", format="{time}, {level}, {message}", level="DEBUG", rotation="10 KB", compression="zip")

with open('data.json') as f:
    data = json.load(f)


head = """Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------"""



@logger.catch
def find():
    print(head)
    for i in data["imdata"]:
        in_1 = i["l1PhysIf"]["attributes"]["dn"]
        in_2 = i["l1PhysIf"]["attributes"]["speed"]
        in_3 = i["l1PhysIf"]["attributes"]["mtu"]
    # logger.debug(print(f"{in_1:71} {in_2}  {in_3:^7}"))
        print(f"{in_1:71} {in_2}  {in_3:^7}")

a = 1
find()

# Generator to generate squares of numbers up to N
def generate_squares(N):
    for i in range(N+1):
        yield i*i

# Program to print even numbers between 0 and n
def print_even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i, end=', ')

# Generator function to yield numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Generator function to yield squares of numbers from a to b
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

# Generator function to return all numbers from n down to 0
def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

if __name__ == "__main__":
    # Test print_even_numbers
    num = int(input("Enter a number (n) to print even numbers between 0 and n: "))
    print("Even numbers between 0 and", num, "are:")
    print_even_numbers(num)
    print()  # For a new line

    # Test divisible_by_3_and_4
    num_2 = int(input("Enter a number (n) to find numbers divisible by 3 and 4 between 0 and n: "))
    print("Numbers divisible by 3 and 4 between 0 and", num_2, "are:")
    for num in divisible_by_3_and_4(num_2):
        print(num, end=', ')
    print()  # For a new line

    # Test squares generator
    a = int(input("Enter starting number (a) for squares: "))
    b = int(input("Enter ending number (b) for squares: "))
    print("Squares from", a, "to", b, "are:")
    for square in squares(a, b):
        print(square, end=', ')
    print()  # For a new line

    # Test numbers_down_to_zero generator
    num_3 = int(input("Enter a number (n) to count down to 0: "))
    print("Counting down from", num_3, "to 0:")
    for num in numbers_down_to_zero(num_3):
        print(num, end=', ')

import math

def degree_to_radian(degrees):
    radians = degrees * (math.pi / 180)
    return radians

def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

def polygon_area(sides, length):
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    return area

def parallelogram_area(base, height):
    area = base * height
    return area

def main():
    # Convert degree to radian
    degree = 15
    radian = degree_to_radian(degree)
    print("Input degree:", degree)
    print("Output radian:", radian)
    print()

    # Calculate trapezoid area
    base1 = 5
    base2 = 6
    height_trap = 5
    area_trap = trapezoid_area(base1, base2, height_trap)
    print("Height of trapezoid:", height_trap)
    print("Base, first value:", base1)
    print("Base, second value:", base2)
    print("Trapezoid area:", area_trap)
    print()

    # Calculate polygon area
    sides = 4
    length_side = 25
    area_polygon = polygon_area(sides, length_side)
    print("Input number of sides:", sides)
    print("Input the length of a side:", length_side)
    print("Polygon area:", area_polygon)
    print()

    # Calculate parallelogram area
    base_parallelogram = 5
    height_parallelogram = 6
    area_parallelogram = parallelogram_area(base_parallelogram, height_parallelogram)
    print("Length of base:", base_parallelogram)
    print("Height of parallelogram:", height_parallelogram)
    print("Parallelogram area:", area_parallelogram)

if __name__ == "__main__":
    main()
