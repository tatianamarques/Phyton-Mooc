maximum = 10
releve = int(input())
if releve == 0:
    print("Pas de pluie aujourd'hui")

elif releve > maximum:

    maximum = releve
    print ("Nous avon un noveau record.")
    
else:
    print("Pas de nouveau record")
print ("Maximum retenu: ", maximum)


