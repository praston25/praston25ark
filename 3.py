import sys

# Mengambil input
people = int(input("Jumlah Orang Yang Jabat Tangan: "))

# Menampilkan output
##print ("Jumlah", people)
a = 0
list (range(people))
for x in list (range(people, 0, -1)):
    ##print (x)
    list (range(x))
    for y in list (range(x-1, 0, -1)):
        ##print (x, y)
        a+=1
    
print ("Jumlah Jabat Tangan :", a)
