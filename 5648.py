import sys

lst = []
n = sys.stdin.readlines()

for i in n:
    for j in i.split():
        lst.append(int(j[::-1]))

lst = lst[1:]
lst.sort()
print("\n".join(map(str, lst)))