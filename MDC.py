import math

x = int (input())
y = int (input())

MDC= math.gcd(x,y)

print (MDC)

# Sem chamar a função gdc

x = int(input("x = "))
y = int(input("y = "))
while y > 0:
    x, y = y, x % y
    print(x, y)
print("pgcd = ", x)