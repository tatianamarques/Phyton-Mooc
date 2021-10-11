"""
Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} 
(la racine carrée du produit de a par b) de deux nombres positifs a et b de type float 
lus en entrée.

Si au moins un de ces nombres est strictement négatif, le programme imprime 
le texte « Erreur ».

(Importando o negativo "print erreur" não funciona)
import math

a = float(input())
b = float(input())

raiz = math.sqrt(a*b)

print (raiz)


"""

a = float(input())
b = float (input())
raiz = float(a*b) ** 0.5
if a < 0 or b < 0:
    print ("Erreur")
else:
    print(raiz)


