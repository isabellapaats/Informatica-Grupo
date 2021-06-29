#Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.
#Para finalizar, es útil saber si un string está escrito completamente en letras minúsculas o en mayúsculas. Para ello disponemos de los métodos 
#islower() e isupper() , respectivamente. Lo mismo es aplicable a isupper() : devuelve True cuando todas las letras están en mayúsculas y al menos hay una letra en 
#la cadena.
string = input("ingrese una palabra: ")

def mayusc_minusc (string):
    if (string[0].islower()) == True:
        return print("la primer letra es minuscula")
    else: print("la primer letra es mayuscula")

print (mayusc_minusc(string))
