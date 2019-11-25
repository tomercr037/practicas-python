conjuntoA= int (raw_input ("Tamanio del conjunto A"))
conjuntoB= int (raw_input ("Tamanio del conjunto B"))
rango= range (0,conjuntoA)
rango1= range (0,conjuntoB)
listaA = []
listaB = []
listai = []
listaU = []
for elemento in rango: 
	num=(raw_input("Ingrese el dato %s del conjunto A" %(elemento)))
	listaA.append(num)
for elemento in rango1:
	num1= (raw_input ("Ingrese el dato %s del cponjunto B" %(elemento)))
	listaB.append(num1)

print ("Los datos del conjunto A: %s" % (listaA))
print ("Los datos del conjunto B: %s" % (listaB))

for elemento in listaA:
	if elemento in listaB:
	listai.append(elemento)
print ("La insercion de A y B es: %s" % (listai))

listaA.extend([element for element in listaB if element not in listaA])
print ("La union del conjunto A y B es: %s" %(listaA))



