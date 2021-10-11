"""
Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun 
des deux n’est un diviseur de l’autre.

"""

a = int(input())
b = int(input())

if a % b == 0 or b % a == 0:
    print ("False")
else:
    print ("True")





    