#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
import re
texto = (r'C:\Users\Martu\Documents\2021\Informatica\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt')

def texto (archivo):
      contador = 0
      with open(archivo,'r') as file:
          for i in file:
              if i[0] != 'P':
                  contador += 1  
              
print("cantidad de lineas:", contador)
      



