#Ejercicio 10
#Escribí un programa que añada a un archivo dado todos los 
#archivos de texto (.txt) que hayan en una determinada 
#carpeta.
import glob
path = r'C:\Users\Intel\Desktop\fundamentos'
archivo = r'C:\Users\Intel\Desktop\fundamentos\completo.txt'
with open(archivo,'a') as file:
    archivos = glob.glob(path +'/*.txt')
    for texto in archivos:
        with open(texto,'r') as text:
           todo = text.read()
           with open(archivo,'a') as final:
            final.write(todo)