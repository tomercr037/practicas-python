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

print 'Ingrese su matriz 1'
for i in range(filas1):
	for j in range (columnas1):
		matriz1[i][j] = int(raw_input('Elemento (%d,%d): '% (i,j)))
print matriz1 
	
print 'Ingrese su matriz 2'
for i in range(filas2):
	for j in range (columnas2):
		matriz2[i][j] = int(raw_input('Elemento (%d,%d): '% (i,j)))
print matriz2

matriz3 = []
for i in range (filas1):
	matriz3.append ( [0] * columnas2)

for i in range (filas1):
	for j in range(columnas2):
		matriz3[i][j] = matriz1[i][j] * matriz2[j][i]

print('La matriz resultante es:')
print matriz3



