"""
Para fazer comentários longos usam-se três aspas duplas abrindo e 
três aspas duplas fechando. Pra fazer comentário de linha é só umas a #
l’auteur : Tatiana Marques

la date: 03 de setembro de 2021

le but du programme: Calcular quantidade de ingredientes de acordo com o número de convidados.

"""

#Variables
invites = float (input("Combien d'invités ? ")) #les données reçues
oeufs = invites * 0.75
chocolat = invites * 25
sucre_vanille = invites * 0.25

#les résultats affichés
print ("Les quantités d’ingrédients pour la préparation de la mousse au chocolat pour " , int (invites) , " invités sont:")
print ("Oeufs: ", int(oeufs))
print ("Chocolat: " , int(chocolat))
print ("Sucre Vanille: " , int(sucre_vanille) )

