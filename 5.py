import sys

numb = 10,2,11,20,3,8

a = list(range(len(numb)))
b = list(numb)
print (a)
for x in a:
    print (x)
    for y in list(range(a, 0, -1)):
        print (x, y)
