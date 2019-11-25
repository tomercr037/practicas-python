from numpy import arange
import matplotlib.pyplot as plt
import math 
import random 


def biseccion():
	fx = raw_input('ingrese la funcion a resolver')
	maximoIteraciones = int(raw_input('ingrese maximo de iteraciones a realizar'))
	a=-1.0
	b=1.0

	while 1:
		x = a
		fa = eval(fx)
	
		x=b
		fb = eval(fx)

		if (fa<0 and fb>0) or (fa>0 and fb<0):
			break
		else:
			a-=1
			b+=1
	print ("El intervalo es: %s,%s" %(a,b))
	irango = arange(a,b,0.001)

	rango = range(1, maximoIteraciones+1)

	for i in rango:
		print "La iteracion" + str(i) + "\n"
		x=a
		fa=eval(fx)
		x=b
		fb=eval(fx)
		m=((a+b)/2)
		fm=eval(fx)

		print "a=%s, fa=%s"%(a,fa)
		print "b=%s, fb=%s"%(b,fb)
		print "m=%s, fm=%s"%(m,fm)

	if fm<0:
		if fa>0:
			b=m
		else:
			a=m
	else:
		if fa<0:
			b=m
		else:
			a=m

	#print "\n\t" + str(a) + "-" + str(b)
	#print "\t--------------------"
	#print "\t	 2"

	iIntervalo=[]

	for x in irango:
		y=eval(fx)
		iIntervalo.append(y)

	plt.plot(irango,iIntervalo)
	plt.grid(axis='both')
	plt.show() 

def graficar():
	fx = "(((5*(x))**2)-(math.e**(x)))"
	rango = arange(-10, 10)
	valores = []

	for x in rango :
		y = eval(fx)
		valores.append(y)
		print "x= "+ str(x)+ "\t y=" + str(y)

	plt.plot(rango,valores)
	plt.grid(axis = 'both')
	plt.show()

def aprox():
	fx= raw_input ('ingrese la funcion a resolver g(x)\t')
	tolerancia= float(raw_input("Ingresa la tolerancia  \t"))

	a=float(raw_input("Ingresa intervalo a \t"))
	b=float(raw_input("Ingresa intervalo b \t"))

	x0=(a+b)/2.0

	print ("La aproximaxion inicial es: %s"%(x0))

	error = tolerancia+1
	x=x0
	while error>tolerancia:
		ga = eval(fx)
		print ("g(a)= %s" %(ga))
		error= abs(ga-x)
		print ("ERROR= %s"%(error))
	
		x = ga

def mat():
	print("ingresa el orden de la matriz 1")
	filas1,columnas1 = int (input()), int(input())
	print("ingresa el orden de la matriz 2")
	filas2,columnas2 = int(input()), int (input())

	if (columnas1==filas2):
		matriz1=[]
		for i in range(filas1):
			matriz1.append ( [0] * columnas1)
	
		matriz2=[]
		for i in range(filas2):
			matriz2.append ( [0] * columnas2)

	print 'La matriz 1 es: '
	for i in range(filas1):
		for j in range (columnas1):
			matriz1[i][j] = (random.randrange(100))
	print matriz1 
	
	print 'La matriz 2 es:'
	for i in range(filas2):
		for j in range (columnas2):
			matriz2[i][j] = (random.randrange(100))
	print matriz2

	matriz3 = []
	for i in range (filas1):
		matriz3.append ( [0] * columnas2)

	for i in range (filas1):
		for j in range(columnas2):
			matriz3[i][j] = matriz1[i][j] * matriz2[j][i]

	print('La matriz resultante es:')
	print matriz3


while True:
	print "*************************************************"
	print "*          PRACTICAS METODOS NUMERICOS          *"
	print "*   ALUMN@ : DANIELA MICHELLE ESQUIVEL ACEVEDO  *"
	print "*          	 GRUPO: ISC151                  *"
	print "*************************************************"

	opc = int (raw_input('Elige una opcion: \n\t 1. Metodo de biseccion \n\t 2. Graficar ecuacion \n\t 3. Metodo de aproximacion \n\t 4. Multiplicacion matrices \n\t 5. Salir\n\t'))

	if opc == 1:
		biseccion()

	if opc == 2:
		graficar()

	if opc == 3:
		aprox()

	if opc == 4:
		mat()

	if opc == 5:
		break

	
