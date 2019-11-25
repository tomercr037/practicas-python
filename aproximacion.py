from numpy import arange
import matplotlib.pyplot as plt
import math 

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
	
#math.sqrt(math.e**(x)/5)
