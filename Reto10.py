# Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
listNum = []
cantidad=int(input(("Ingrese la cantidad de valores a promediar: ")))
# Pedir los numeros a añadir en la lista
for i in range(cantidad):
    listNum.append(float(input(("Ingrese el " + str(i+1) +" número a promediar: "))))
#Promedio
print("El promedio es: "+str(sum(listNum)/len(listNum)))
# Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
listNumVectorA = []
listNumVectorB = []
prodPunto = []
# Pedir los numeros del primer vector
for i in range(3):
    listNumVectorA.append(float(input(("Ingrese el " + str(i+1) +" número del primer vector: "))))
# Pedir los numeros del segundo vector
for i in range(3):
    listNumVectorB.append(float(input(("Ingrese el " + str(i+1) +" número del segundo vector: "))))
for i in range(3):
    prodPunto.append(float(float(listNumVectorA[i])+float(listNumVectorB[i])))
 
print("El producto punto es: "+str(prodPunto))