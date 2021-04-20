# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que 
# imprima cuántas líneas no empiezan con "P").

def texto (archivo):
    contador = 0
    with open(archivo,'r') as file:
        for i in file:
            if i[0] != "P":
                contador += 1
    print ("las lineas que no empiezan con P son: ", contador)

texto(r"/Users/isabellapaats/Desktop/Segundo/Fundamentos_de_Informatica/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt")