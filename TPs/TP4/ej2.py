#Escribí un programa que lea un archivo e imprima las primeras n líneas.

import re
path = r"/Users/isabellapaats/Desktop/Segundo/Fundamentos_de_Informatica/UCEMA_Fundamentos_de_informatica/Python_intro/manipulacion_archivos.txt"
def texto (archivo):
    contador = 0
    with open(archivo,'r') as file:
        for i in file:
            if i[0] != "P":
               contador += 1
    print("La cantidad de líneas que no empiezan con P son:", contador)
     
texto(path)