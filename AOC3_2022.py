#!/usr/bin/python

#Problem: strings halbieren und gemeinsamen case sens. buchstaben finden und werten

with open('AOC3.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",") #transormieren des obigen strings in liste, gesplittet nach ","
win ={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26,
"A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}
score=0 #setzen der punkte als dic, setzen des zaehlers
for k in mylist:
	one = k[:int(len(k)/2)]		#aufspalten in 2 teile
	two = k[int(len(k)/2):]	
	i = 0
	while i < len(one):
		if one[i] in two:		#durchsuchen der elemente von teil 1 in teil 2
			score += win[one[i]]
			i=len(one)
		i+=1

print("Aufgabe 1:",score)

score =0
z=0
while z < int(len(mylist)/3):		#vergleich von 3 eintraegen, intersection sucht in sets, danach zurueck zu string
	a = set(mylist[z*3]).intersection(set(mylist[z*3+1]),set(mylist[z*3+2]))
	score +=win["".join(a)]
	z += 1

print("Aufgabe 2:",score)