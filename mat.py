print ('ingrese dimension de la matriz a')
fila1,columna1= int (input()), int (input())

print ("ingrese dimension de la matriz b") 
fila2, columna2= int (input()), int (input())

if(columna1==fila2):
	matriza =[]
	for i in range(fila1):
		matriza.append([0]*columna1)
	matrizb =[]
	for i in range(fila2):
		matrizb.append([0]*columna2)
print 'ingresa la matriz a'
for i in range (fila1): 
	for j in range (columna1):
		matriza[i][j]= int (raw_input('elemento(%d,%d):'%(i,j)) )
print matriza

print 'ingresa la matriz b'
for i in range (fila2): 
	for j in range (columna2):
		matrizb[i][j]= int (raw_input('elemento(%d,%d):'%(i,j)) )
print matrizb

matrizc=[]
for i in range(fila1):
	matrizc.append([0]*columna2)
for i in range (fila1):
	for j in range (columna2):
		matrizc[i][j]= matriza[i][j]*matrizb[j][i]
print 'la matriz es:'
print matrizc 

