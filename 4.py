import sys

str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890"
#test string
#str2 = "hari apa saja saya bisa!"
str2 = input()
a = list(range(len(str1)))
b = list(range(len(str2)))
c = list (str1)
arry = []
d = "Tidak ada karakter yang berulang"
for x in b :
    for y in a :
        arry.extend([0])
        if (list(str2)[x] == list(str1)[y]):
            #test apakah urutan di str1 masuk atau tidak
            #print ("match", x, y)
            arry [y] += 1
            
#test apakah nilai arry sudah masuk atau belum           
#print (arry [0])
for y in a :
    if (arry [y] > 1) :
        print (c[y], ":", arry [y])

exit ()
