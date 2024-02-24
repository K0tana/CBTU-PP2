n = int(input())
a = ([int(input()) for _ in range(n)])
print(len(([i for i in a if i < 0])))