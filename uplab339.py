#continuar tentando

parier = int(input())
sorti = int(input())

mise = 10

numsortant = 12 * mise
pair_impair = 2 * mise
couleur = 2 * mise

if parier > 0 and parier <= 12 and parier == sorti:
    print (numsortant)
elif parier != sorti and parier <=12 and sorti <=12:
    print ("0")
    
if parier == 13 or parier ==  14:
    print (pair_impair)
elif parier == 15 or parier == 16:
    print (couleur)
