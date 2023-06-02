# leer el archivo, agregar contenido, modificar una linea
from os import system

def leer_archivo(ruta):
    with open (ruta,'r') as elarchivo:
        for linea in elarchivo:
            print (linea)


def agregar_texto(ruta, nueva_linea):
    archivo = open(ruta, 'a')
    archivo.write(nueva_linea)
    archivo.close()

def modificar_linea(ruta,numero_linea,nueva_linea):
    archivo = open(ruta, 'r')
    lineas=archivo.readlines()
    archivo.close()
    print(len(lineas))
    if numero_linea <=len(lineas):
         lineas[numero_linea-1]=nueva_linea
    else:
         print("el numero de linea esta fuera de rango")
    archivo = open(ruta, 'w')
    archivo.writelines(lineas)
    archivo.close()



while True:
    system('cls')
    opcion=int(input('Seleccione la operacion que desea realizar: 1. leer, 2. agregar texto, 3. modificar linea: '))
    if opcion==1:
        leer_archivo('Establecimientos_salud.txt')
        input()
    elif opcion==2:
        numero=input("Ingrese el numero de establecimiento: ")
        nombre=input("Ingrese el nombre de establecimiento: ")
        localidad = input("Ingrese la localidad de establecimiento: ")
        provincia = input("Ingrese la provincia de establecimiento: ")
        nueva_linea=numero+'\t'+nombre+'\t'+localidad+'\t'+provincia+'\n'
        agregar_texto('Establecimientos_salud.txt',nueva_linea)
    elif opcion==3:
        numero_linea=int(input("Ingrese el umero de linea que desea modificar: "))
        numero = input("Ingrese el numero de establecimiento: ")
        nombre = input("Ingrese el nombre de establecimiento: ")
        localidad = input("Ingrese la localidad de establecimiento: ")
        provincia = input("Ingrese la provincia de establecimiento: ")
        nueva_linea = numero + '\t' + nombre + '\t' + localidad + '\t' + provincia + '\n'
        modificar_linea('Establecimientos_salud.txt',numero_linea,nueva_linea)
