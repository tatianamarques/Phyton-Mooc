import random
secret = random.randint(0, 5)
devinette = int (input ("Deviner la valeur choisie?"))
if devinette== secret:
    print ( "Gagné !")

else: 
    print ("Perdu !  La valeur était ", secret)

