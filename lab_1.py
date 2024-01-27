# syntax
print("Hello World")
if 5 >= 4:
    print("YES")


# comments
"""THE FIRST AVATAR MOVIE WASN'T SO GOOD AS PEOPLE SAY """
""" This is comment too"""

# variables
a1, b1 = 5, 6
a = b, c = d = 5, 6
s = "gigitigag"
print(a1 + b1)
print(s * 3)
print(s, "seems you win {}".format(input("\nyour name:")))
print(a, b, c, d)


# numbers
a = 5.456342
print(a)
print(int(a))
print(complex(a))
print(a - int(a) + complex(a))


# random variables
a = "textes"
b = ["a", "b", "c"]
c = 20.5
d = 5 + 3j
e = {"class" : "Autobot", "weapon": "glass gas cannon", "name": "clifjumper"}


# data types

f = [a, b, c, d, e]
print([type(i) for i in f])


# strings
p = "HelLo wOrlD"
print(p.lower())
print(p.upper())
print(p.strip())
print(p.split())
