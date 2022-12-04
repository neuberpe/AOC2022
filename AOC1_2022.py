#!/usr/bin/python
#Groesste Summe Bloecke

with open("AOC1.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",") #transormieren des obigen strings in liste, gesplittet nach ","
z = 0
a = 0
s = []
for k in mylist:	#ersatz des leeren eintrags gegen null, damit umwandeln in int moeglich
	if k == "":
		mylist[z] = "0"
	z += 1
mylist = [int(e) for e in mylist] #wandelt liste von strings in liste von zahlen um

#Teil 1
mylist.append(0) #fuer den abschluss der nachfolgenden schleife ist die 0 am schluss notwendig
for x in mylist:
	if x > 0:
		a = a + x
	else:
		s.append(a)
		a = 0

print(max(s))	#maxwert

#Teil 2
s.sort()
l = len(s)
print(s[l-1]+s[l-2]+s[l-3])	#summe der 3 groessten
