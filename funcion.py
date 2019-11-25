from numpy import arange
import matplotlib.pyplot as plt
import math 

fx = "((x**3)-(6*(x**2))+(11*x)-6.1)"
rango = arange(-10, 10, 0.001)
valores = []

for x in rango :
	y = eval(fx)
	valores.append(y)
	print "x= "+ str(x)+ "\t y=" + str(y)

plt.plot(rango,valores)
plt.grid(axis = 'both')
plt.show()
#(3**(math.sqrt((10*x)+(5)))
#((1)/(math.sqrt((5*x)+6)))
