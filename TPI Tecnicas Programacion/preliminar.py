import pickle
from os import system

class alumnoColegio:
    def __init__(self):
        print ('Ingrese los Datos:')
        self.dni = input('DNI: ')
        self.nombre = input('Nombre: ')
        self.apellido = input('Apellido: ')
        self.direccion = input ('Direccion: ')
        print ('Se ha creado el alumno {}'.format(self.apellido))

    def __str__(self):
        return ('DNI: {}\nNombre: {}\nApellido: {}\nDireccion: {}'.format(self.dni,self.nombre,self.apellido,self.direccion))


def lista():
    for item,alu in enumerate(colegio):
        print ('____________')
        print ('alumno: ',item+1)
        print(alu)


def baja(instituto):
    num = int(input('Ingrese el número del alumno que quiere dar de baja: '))-1
    print('\n\nQuiere dar de baja a {}? S/N'.format(instituto[num]))
    resp = input('==> ').lower()
    if resp == 's':
        instituto.pop(num)
    elif resp == 'n':
        print ('No se ha modificado el listado')
    else:
        print('No eligió una opcion correcta')

    input ('Presione "ENTER" ')

    return instituto

def modifica(instituto):
    num = int(input('\nIngrese el número del alumno que quiere Modificar: '))-1
    print ('\n{}\n'.format(instituto[num]))
    resp = input('\nModifica S/N? ').lower()
    if resp =='s':
        print (instituto[num].dni)
        cambio = ''
        cambio = input('Nuevo valor? (ENTER no cambia)')
        if cambio != '':
            instituto[num].dni = cambio
        print (instituto[num].nombre)
        cambio = ''
        cambio = input('Nuevo valor? (ENTER no cambia)')
        if cambio != '':
            instituto[num].nombre = cambio
        print (instituto[num].apellido)
        cambio = ''
        cambio = input('Nuevo valor? (ENTER no cambia)')
        if cambio != '':
            instituto[num].apellido = cambio
        print (instituto[num].direccion)
        cambio = ''
        cambio = input('Nuevo valor? (ENTER no cambia)')
        if cambio != '':
            instituto[num].direccion = cambio
    return instituto

try:
    with open('archivocolegio','rb') as targa:
            colegio = pickle.load(targa)
except FileNotFoundError:
    colegio = []

opc = ''
while opc != '***': 
    system ('cls')
    
    menu = """
    Ingrese la opcion deseada:
    1.- Alta de alumno
    2.- Lista de alumnos
    3.- Baja de un alumno
    4.- Modifica Alumno
    ***.- Salir"""

    print (menu)
    opc = input('====>>> ')
    if opc != '***':
        match opc:
            case '1':
                alumnoNuevo = alumnoColegio()
                colegio.append(alumnoNuevo)
            case '2':
                lista()                
                input('Presione "ENTER"')

            case '3':
                lista()
                colegio = baja(colegio)
            case '4':
                lista()
                modifica(colegio)
            

    else:
        with open('archivocolegio','wb') as targa:
            pickle.dump(colegio,targa)