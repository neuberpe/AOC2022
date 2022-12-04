#!/usr/bin/python

#Problem: ueberlagerungen von bereichen ausfindig machen

with open('AOC4.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",")

i=0
z=0
z2=0
while i < len(mylist):
	a = list(range(int(str(mylist[i])[:mylist[i].find("-")]),int(str(mylist[i])[mylist[i].find("-")+1:])+1))
	b = list(range(int(str(mylist[i+1])[:mylist[i+1].find("-")]),int(str(mylist[i+1])[mylist[i+1].find("-")+1:])+1))
	if set(a).issubset(b) or set(b).issubset(a):
		z+=1
	if bool(set(a) & set(b)):
		z2+=1
	i+=2

print("Aufgabe 1:",z)
print("Aufgabe 2:",z2)