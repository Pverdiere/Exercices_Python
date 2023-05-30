nb1 = int(input("Veuillez indiquer un nombre : "))
nb2 = int(input("Un deuxième : "))
nb3 = int(input("Et un troisième : "))

max1_2 = nb1 if nb1 > nb2 else nb2

print("Le nombre la plus grands est", max1_2 if max1_2 > nb3 else nb3)