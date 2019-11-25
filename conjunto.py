a=[]
b=[]

num = int (raw_input ("ingrese el numero de arreglo A"))
rango= range(0,num)
for i in rango:
	numero = (raw_input("ingrese el valor de conjunto A" + str(i)))
	a.append(numero)

num = int (raw_input ("ingrese el numero de arreglo B"))
rango= range(0,num)
for i in rango:
	numero = (raw_input("ingrese el valor de conjunto B" + str(i)))
	b.append(numero)

print "a=%s"%a
print "b=%s"%b
