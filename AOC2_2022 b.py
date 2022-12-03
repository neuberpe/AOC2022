#!/usr/bin/python

#Problem: Schere Stein Papier, Punkte aus strategie

with open('AOC2.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",") #transormieren des obigen strings in liste, gesplittet nach ","
s = 0
win = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z":6}

for k in mylist:	#suche und addieren der Werte aus dem dictonaries
	s = s + win[k]

print("Punkte Aufgabe 1:",s)
s = 0

win = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z":7}

for k in mylist:
	s = s + win[k]

print("Punkte Aufgabe 2:",s)