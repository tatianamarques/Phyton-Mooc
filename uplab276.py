"""Écrire un programme qui imprime la valeur du volume 
d’une sphère de rayon r, float lu en entrée.
On rappelle que le volume d’une sphère de rayon r est donné par la formule : \frac{4}{3}\pi{r^3}
"""
from math import pi
r = float(input())
ve = (4*pi*r**3)/3
print (ve)
