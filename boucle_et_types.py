import random
def sapin(n):
    for i in range(n):
        line = ""
        for y in range(i+1):
            line += "#"
        print(line)

#nb = int(input("nombre : "))
#sapin(nb)

def sumList(list):
    sum = 0
    for cel in list:
        sum += cel
    return sum

# print(sumList([8,80,2,1]))

def moyList(list):
    sum = 0
    for cel in list:
        sum += cel
    return sum / len(list)

# print(moyList([8,80,2,1]))

#for i in range(100):
#    console = ""
#    text = False
#    if (i + 1) % 3 == 0 :
#        console += "Fizz"
#        text = True
#    if (i + 1) % 5 == 0 :
#        console += "Fuzz"
#        text = True
#    if text :
#        print(console)
#    else :
#        print(i + 1)

def invList(list):
    newList = [0] * len(list)
    for cel in enumerate(list):
        newList[len(list) - (cel[0] + 1)] = cel[1]
    print(newList)

# invList(["Hey", "Ho", "Hissez", "haut"])

#dictionnaire = {
#    "voiture" : "Véhicule motorisé à 4 roues",
#    "vélo" : "Véhicule à 2 roues non motorisé",
#    "avion" : "C'est pour volé",
#    "moto" : "Véhicule motorisé à 2 roues"
#}
#
#mot = input("Un mot : ")
#
#if mot in dictionnaire :
#    print(dictionnaire[mot])
#else:
#    print("Connais pas")

liste = [random.randrange(0,100) for i in range(1000)]

print(liste)

newListe = [x for x in liste if x < 10]

print(newListe)