archivo = raw_input ("Ingresa el archivo:")
archivo = open(archivo, 'r')

datos = archivo.read()

for linea in datos.split ('\n'):
	#print "Linea: %s" %(linea)
		operacion = linea.split('')
		operando = None

	if len(operacion) == 2:
		operando = operacion[1]

	operacion = operacion[0]

	print "operacion: %s, operando: %s" %(operacion, operando)

