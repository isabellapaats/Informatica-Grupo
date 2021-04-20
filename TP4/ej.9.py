#Ejercicio 9
#Realizá un programa que lea un archivo y obtenga la frecuencia de 
# cada palabra que hay en el archivo. Recordá que la frecuencia es 
# la relación entre número de veces que aparece la palabra en 
# cuestión con respecto a la cantidad total de palabras.

path = r'C:\Users\Intel\Desktop\fundamentos\manipulacion_archivos.txt'
lista =[]
lista2 =[]
lista3 ={}
with open(path,'r') as file:
    for lineas in file:
        lista.extend(lineas.split())
    for palabra in lista:
        sin_coma = palabra.strip(",")
        lista2.append(sin_coma)
    print("Hay", len(lista2), "palabras")
    for i in lista2:
        if i in lista3:
            lista3[i] +=1
        else:
            lista3[i] = 1
    for e in lista3:
        frecuencia = lista3[e]/len(lista3)
        print("La palabra", e, "aparece con una frecuencia de ", round(frecuencia,4),"apareciendo un total de", lista3[e], "vez/veces")