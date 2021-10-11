annee = int(input("Donnez l'année à tester :"))
if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print('bissextile')
else:
    print('non bissextile')
