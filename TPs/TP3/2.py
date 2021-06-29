''' Escribí un programa que verifique si un string tiene 
todos sus caracteres permitidos. Estos caracteres son a-z, 
A-Z y 0-9.'''



texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet2."
patron = "[a-zA-Z0-9]" #los rangos al unirlos van pegados

import re 
def programa_verificador2(patron, texto):
    if re.findall (patron, texto):
        print("Verificado")
    else:
        print("NO verif")

programa_verificador2(patron, texto)

def caracteres_permitidos(string):
  return not bool(re.search('[^a-zA-Z0-9]', string))

print("El string", "ABCDEF")