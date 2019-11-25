
suma=0
total=10
lista=[]
cont=0
cont2=0
Mayor=0
menor=0

print ("Ingresa tus 10 calificaciones")
for i in range (1,11):
	numero=int (input ("%d:"%(i)))
	lista.append(numero)
	suma= suma+numero
total=suma/11
print("el promedio es %d"%(total))
Mayor= max(lista)
menor=min(lista)
print ("la calificacion mayor es %s"% (Mayor))
print ("la calificacion menor es %s" % (menor))
for lista in lista:
	if lista >=70:
	  cont= cont+1
	else:
	  cont2=cont2+1
print ("las calificaciones aprobatorias son %s" % (cont))
print ("las calificaciones reprobatorias son %s" %(cont2))


