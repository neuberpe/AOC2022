#!/usr/bin/python

#Problem: Elemente umschlichten, one by one und in gruppen

with open('AOC5.txt', 'r') as file:
    data = file.read().replace('\n', ',')
mylist = data.split(",")

container = [["N","W","F","R","Z","S","M","D"],["S","G","Q","P","W"],["C","J","N","F","Q","V","R","W"],["L","D","G","C","P","Z","F"],
 ["S","P","T"],["L","R","W","F","D","H"],["C","D","N","Z"],["Q","J","S","V","F","R","N","W"],["V","W","Z","G","S","M","R"]]

for k in mylist:
	for i in range(0,int(k[5:k.find("from")])):		#wie oft genommen wird
		container[int(k[k.find("to")+3:])-1].insert(0,container[int(k[k.find("from")+5:k.find("to")])-1][0])	#auf stapel a von stapel b
		del container[int(k[k.find("from")+5:k.find("to")])-1][0]

print("Aufgabe 1:", end="")
for c in range(0,len(container)):
	print(container[c][0], end="")
print()

container = [["N","W","F","R","Z","S","M","D"],["S","G","Q","P","W"],["C","J","N","F","Q","V","R","W"],["L","D","G","C","P","Z","F"],
 ["S","P","T"],["L","R","W","F","D","H"],["C","D","N","Z"],["Q","J","S","V","F","R","N","W"],["V","W","Z","G","S","M","R"]]

for k in mylist:
	greifer =[]
	for i in range(0,int(k[5:k.find("from")])):		#wie oft genommen wird
		greifer.insert(0,container[int(k[k.find("from")+5:k.find("to")])-1][0])	#auf greifer von stapel b
		del container[int(k[k.find("from")+5:k.find("to")])-1][0]
	for j in range(0,len(greifer)):					#greifer wird in reihenfolge wieder abgegeben
		container[int(k[k.find("to")+3:])-1].insert(0,greifer[j])

print("Aufgabe 2:", end="")
for c in range(0,len(container)):
	print(container[c][0], end="")
print()