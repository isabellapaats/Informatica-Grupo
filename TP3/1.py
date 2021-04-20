'''Ejercicio 1
Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son
a-z, A-Z y 0-9.'''

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet2."
patron = "[a-zA-Z0-9]" #los rangos al unirlos van pegados


import re
def programa_verificador(patron, texto):
  if re.search(patron, texto):
    print("Verificado")
  else:
    print("No verificado") 
programa_verificador(patron, texto) #llamar la función

