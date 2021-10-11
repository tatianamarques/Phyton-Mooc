DISTANCE = 3.844e8
nombre_pliages = 0
epaisseur = 0.0001
while epaisseur < DISTANCE :
    nombre_pliages = nombre_pliages + 1
    epaisseur = 2 * epaisseur
print ('Nombre de pliages nécessaires: ',  nombre_pliages)
