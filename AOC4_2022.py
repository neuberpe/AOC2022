#!/usr/bin/python

#Problem: ueberlagerungen von bereichen ausfindig machen

with open('AOC4.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",")

i=0
z=0
z2=0
while i < len(mylist):	#zuerst werden ganze listen aus den angaben gemacht mit range und string checks
	a = list(range(int(str(mylist[i])[:mylist[i].find("-")]),int(str(mylist[i])[mylist[i].find("-")+1:])+1))
	b = list(range(int(str(mylist[i+1])[:mylist[i+1].find("-")]),int(str(mylist[i+1])[mylist[i+1].find("-")+1:])+1))
	if set(a).issubset(b) or set(b).issubset(a):	#ueberprueft, ob eine liste in einer anderen liste vollständig enthalten ist
		z+=1
	if bool(set(a) & set(b)):		#ueberprueft, ob es ueberlappende elemente gibt
		z2+=1
	i+=2

print("Aufgabe 1:",z)
print("Aufgabe 2:",z2)