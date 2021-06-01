print("DWZ-Rechner")

a = input("Alte eigene DWZ: ")
DWZalt = float(a)

b = input("Alter (in Jahren): ")
Alter = float(b)

c = input("Anzahl Spiele: ")
Spiele = float(c)

c_2 = input("Punkte: ")
W = float(c_2)



d = input("DWZ Gegner1: ")
DWZ1 = float(d)

e = input("DWZ Gegner2: ")
DWZ2 = float(e)

f = input("DWZ Gegner3: ")
DWZ3 = float(f)

g = input("DWZ Gegner4: ")
DWZ4 = float(g)

h = input("DWZ Gegner5: ")
DWZ5 = float(h)

i = input("DWZ Gegner6: ")
DWZ6 = float(i)

j = input("DWZ Gegner7: ")
DWZ7 = float(j)

k = input("DWZ Gegner8: ")
DWZ8 = float(k)

l = input("DWZ Gegner9: ")
DWZ9 = float(l)

m = input("DWZ Gegner10: ")
DWZ10 = float(m)



DDWZ = float()
DDWZ = (DWZ1 + DWZ2 + DWZ3 + DWZ4 + DWZ5 + DWZ6 + DWZ7 + DWZ8 + DWZ9 + DWZ10) / Spiele


We = float()
We = 1 / (1 + 10 ** - (DWZalt - DDWZ) / 400)


E0 = float()
J = float()
if Alter <= 20:
	J = 5
elif 20 < Alter <= 25:
	J = 10
else:
	J = 15
E0 = (DWZalt / 1000) + J


fB1 = float()
if Alter > 20:
	fB1 = 1
else:
	if W >= We:
		fb1 = DWZalt / 2000
	else:
		fB1 = 1
fB = float()
if fB1 < 0.5:
	fB = 0.5
elif fB1 > 1.5:
	fB = 1.5
else:
	fB = fB1


SBr = float()
if DWZalt >= 1300:
	SBr = 0
else:
	if W <= We:
		SBr = (2.718281828 ** 1300-DWZalt) / 150 - 1
	else:
		SBr = 0



E1 = float()
E1 = E0 * fB + SBr
E = float()
if E1 < 5:
	E = 5
else:
	if SBr > 0:
		if E1 > 150:
			E = 150
		else:
			E = E1
	else:
		if E1 > 30:
			E = 30
		else:
			E = E







DWZneu = float()
DWZneu = DWZalt + 800 * (W - We) / (E + Spiele)

print("Neue DWZ:")
print(DWZneu)


ende = input()
