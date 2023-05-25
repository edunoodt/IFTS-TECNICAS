from os import system
import platform

def borra():
    siso = platform.system()
    match siso: 
        case 'Windows':
            system ('cls')
        case 'Linux':
            system('clear')

def inicializaPac():
    dicti = {}
    try:
        with open('Clinica/info/pacientes.txt','r') as archi:
            salida = archi.readline()
            while salida != '':
                claveb = True
                clave = ''
                lista = []
                palabra = ''
                for letra in salida:
                    if letra != ';' and letra != '\n':
                        palabra = palabra + letra
                    elif claveb:
                        clave = palabra
                        claveb = False
                        palabra =''
                    else:
                        lista.append(palabra)
                        palabra = ''
                dicti[clave]=lista
                salida = archi.readline()
    except FileNotFoundError:
        archi = open ('Clinica/info/pacientes.txt','w')
        archi.close()
    return dicti

def ingresoDNI():
    print ('\n=============================================================================================')
    print ('El documento debe contener 8 caracteres.  Agregar 0 para documentos con menos digitos\n')
    print (' Para salir del sistema presione "***" ')
    cont = 0
    dni=''
    while len(dni) != 8 and cont < 3 and dni != '***':
        print ('Intento {}'.format(cont+1))
        dni = input ('Ingrese DNI del Paciente ===>>>>  ')
        cont += 1
    if cont == 3:
        print ('*******************************\nVerifique número de documento\n')
        return 'error'
    elif dni == '***':
        return '***'
    else:
        return dni

def verificaDNI(dni,dicti):
    return dni in dicti.keys()

def altaDNI(dni,pac):    
    nombre = input ('Nombre del paciente: ')
    apellido = input ('Apellido del paciente: ')
    nac = input ('fecha de nacimiento (ddmmaaaa): ')
    
    linea = (dni+ ';' + nombre + ';' + apellido + ';' + nac + '\n')
    with open('Clinica/info/pacientes.txt','a') as archi:
        archi.write(linea)

    lista = [nombre,apellido,nac]
    pac[dni]= lista
    return pac

def muestraPac(dni,pac):
    paciente = pac[dni]
    borra()
    print('\n*******************************************************************************')
    print('DNI Nro: {} - Apellido: {} - Nombre: {} - Nacimiento: {}'. format(dni,paciente[1],paciente[0],paciente[2]))
    input('\npresione enter para continuar')


