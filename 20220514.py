#Papp Mihály házi feladat
#2022.05.24.

f = open("file.txt", "a")


def atlag(lista):
    atlag = sum(lista) / len(lista)
    return atlag



try:
    szam = int(input("Egész számokat kérek, kilépés 0-val: "))
except:
    pass

szamok = []
paros_szamok = []
paratlan_szamok = []

while szam != 0:
    try:
        szam = int(input('Egész számokat kérek, kilépés0-val: '))

    except:
        pass

    if szam != 0:
        szamok.append(szam)
        f.write(szam,"\n")


print(f'A számok összege: {sum(szamok)}')
print(f'A számok átlaga: {sum(szamok) / len(szamok)}')

for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        paros_szamok.append(szamok[i])
    else:
        paratlan_szamok.append(szamok[i])


print(f"\n\nLegkisebb páros szám: {min(paros_szamok)}")
print(f"Legnagyobb páros szám: {max(paros_szamok)}")
print(f"Páros számok száma: {len(paros_szamok)}")
print(f"Páros számok növekvő sorrendbe: {paros_szamok.sort()}")

print("\n---------------------------------------------\n")
print(f"Legkisebb páratlan szám: {min(paratlan_szamok)}")
print(f"Legnagyobb páratlan szám: {max(paratlan_szamok)}")
print(f"Páratlan számok száma: {len(paratlan_szamok)}")
print(f"Páratlan számok: {paratlan_szamok }")