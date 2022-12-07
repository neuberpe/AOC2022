#!/usr/bin/python

#Problem: 4 / 14 nacheinanderfolgende unterschiedliche buchstaben finden

with open('AOC6.txt', 'r') as file:
    data = file.read()

def packet(marker):					#funktion weil fuck you angabe
	for i in range(marker,len(data)):
		liste =[]
		for j in range(0,marker):		#zerlegt einen teil des strings in liste
			liste.append(data[i-marker:i][j])
		if len(liste) == len(set(liste)):		#prueft, wann liste uniqe chars hat, sucht position, breakt
			print("".join(liste))
			print(data.find("".join(liste))+marker)
			break

packet(4)
packet(14)