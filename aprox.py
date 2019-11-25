from numpy import *

valor = float (raw_input("valor de aproximacion:"))
numero = int (raw_input("NUMERO DE ITERACIONES EN LA ECUACION:"))

print "LA ECUACION ES  xi - xi** - xi - 2 " 
print "                -------------------"
print "                     2xi  -   1"

rango = range (0,numero)

for elemento in rango:
    valor = (valor - ((valor**2 - valor - 2)/ ((2*valor)-1))) 

    print "LA APROXIMACION ES:  %f" %(valor)

