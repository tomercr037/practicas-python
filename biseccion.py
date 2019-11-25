from numpy import arange
import matplotlib.pyplot as plt

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

