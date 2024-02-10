# boolean is specific type of data that have only two variables:

print(1 == 1)
print(2 == 1)

# it also demands in numeos of operators
while (True):
    print("this sycle if infinite")
    break

# Operators working on variables and values, including arithmetic, logical, membership, and identity operations.


a, b, c = 1, 2, 3
print(a + b)
print(a - c)
print(a // c)
print(b % c)
print(c / b)
for i in range(3):
    print(a - i)
if a == b or a < c:
    print("kinda poor examples")

# List, tuples and sets

cars = ["toyota", "ford", "audi"]
cars.insert(1, "mercedes")
cars[2] = "Mcclaren"
cars.append("Honda")
print(cars[2:6])
print(len(cars))
print(*cars)

inventory = ("bomb", "baby", "AK-47")
print(len(inventory))
print(inventory[0:2])
print(inventory[-1])

computers = {"King_Lenovo", "HP", "samsung"}
smartphones = {"oppo", "Apple", "samsung"}
smartphones.add("huawei")
computers.update(smartphones)
print(*computers)
computers.discard("oppo")

# dictionary
movie = {"name": "Ford vs Ferrari", "genre": "historical", "year": 1921, "time": 204, "actor": "Christian Bale"}

movie["year"] = 2020
movie.pop("actor")
print(movie.get("name"))

# operators if/else

if int(input('Введите число')) % 2 == 0:
    print("Число чётное, либо равно 0 ")
else:
    print("Число не четное")
print("That was true") if 3 == 5 else print("That was fkn lie")

a = 50
b = 10
if a == b:
    print("a == b")

elif a > b:
    print("A is larger")

else:
    print("B is larger")

print(*[x for x in range(10) if x % 2 == 0])
