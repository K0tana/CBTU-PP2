# syntax
print("Hello World")
if 5 >= 4:
    print("YES")
# comments
"""THE FIRST AVATAR MOVIE WASN'T SO GOOD AS PEOPLE SAY """
# variables
a, b = 5, 6
print(a + b)
s = "gigitigag"
print(s * 3)
a = b, c = d = 5, 6
print(s, "seems you win {}".format(input("\nyour name:")))
print(a, b, c, d)
# numbers
a = 5.456342
print(a)
print(int(a))
print(complex(a))
print(a - int(a) + complex(a))
# data types
a = "textes"
b = ["a", "b", "c"]
c = 20.5
d = 5 + 3j
# data types
e = {"class" : "Autobot", "weapon": "glass gas cannon", "name": "clifjumper"}
f = [a, b, c, d, e]
print([type(i) for i in f])
# strings
p = "hello world"
print(p.lower())
print(p.upper())
print(p.strip())
print(p.split())
