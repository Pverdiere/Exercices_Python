def est_pair(nb):
    if nb % 2 :
        print("Le nombre est impair")
    else :
        print("Le nombre est pair")

# nb_utilisateur = int(input("Entrez un nombre entier : "))
# est_pair(nb_utilisateur)

def min(nb1, nb2, nb3):
    min1_2 = nb1 if nb1 < nb2 else nb2
    return min1_2 if min1_2 < nb3 else nb3

#nb1 = int(input("Veuillez indiquer un nombre : "))
#nb2 = int(input("Un deuxième : "))
#nb3 = int(input("Et un troisième : "))
#print(min(nb1, nb2, nb3))

def x(a,b):
    '''retourne la valeur absolue du résultat de la multiplication de a et b'''
    return abs(a*b)

#nb1 = int(input("nombre 1 : "))
#nb2 = int(input("nombre 2 : "))
#print(x(nb1,nb2))

def moyenne(a,b,c):
    return (a + b + c) / 3

nb1 = int(input("Nombre 1 : "))
nb2 = int(input("Nombre 2 : "))
nb3 = int(input("Nombre 3 : "))

print(moyenne(nb1,nb2,nb3))