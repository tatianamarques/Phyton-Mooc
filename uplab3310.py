lettre = str(input())
a = float(input())

tetraedre = (2**0.5)/12 * (a ** 3)

cube = a**3

octaedre = (2**0.5)/3 * (a ** 3)

dodecaedre = (15 + 7 * (5 ** 0.5))/ 4 * (a ** 3)

icosaedre = 5 * (3 + (5 ** 0.5)) / 12 * (a ** 3)

if lettre == "T":
    print (tetraedre)
elif lettre == "C":
    print (cube)
elif lettre == "O":
    print (octaedre)
elif lettre == "D":
    print (dodecaedre)
elif lettre == "I":
    print (icosaedre)
else:
    print ("Polyèdre non connu")
