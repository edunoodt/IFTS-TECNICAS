from os import system



pacientes = {}
opcion =''
while opcion!='***':
    system('clear')
 
    print('Ingrese la opción deseada')
    print('1.- Alta de Paciente')
    print('2.- Modificar datos de paciente')
    print('3.- Eliminar un usuario')
    print('***.- Para salir del sistema')

    opcion = input('Ingrese la opción deseada: ')
    if opcion!='***':
        opcion = int(opcion)
        match opcion:
            case 1:
                dni = input('Ingrese el DNI del paciente sin comas, puntos ni guiones: ')
                nombre = input('Nombre del paciente: ')
                apellido = input('Apellido: ')
                fechaNac = input('Ingrese fecha de nacimiento con formato dd-mm-aaaa: ')
                pacientes[dni]=[nombre,apellido,fechaNac]
                for clave, valor in pacientes.items():
                    print ('DNI {} : Paciente {}'.format(clave,valor))
                input()

            case 2: #modificación de datos del paciente
                dni = input('Ingrese el DNI del paciente a modificar: ')
                #for clave in pacientes.keys():
                if dni in pacientes.keys():
                    print (pacientes[dni])
                    opc = input('Ingrese "N" para nombre, "A" para apellido o "F" para fecha de nacimiento: ').upper()
                    nvo = input('Ingrese nuevo valor: ')
                    match opc:
                        case 'N':
                            pacientes[dni][0]
                        case 'A':
                            pacientes[dni][1]
                        case 'F':
                            pacientes[dni][2]
                    print (pacientes)
                else :
                    print('El DNI ingresado no esta en la base de datos')
                    input()
            case 3:
                dni = input('Ingrese el DNI del paciente a ELIMINAR: ')
                if dni in pacientes.keys():
                    print ('Quiere eliminar ',pacientes[dni])
                    rsp = input('s/n: ').lower()
                    if rsp:
                        del pacientes[dni]
                        print('El paciente has sido eliminado del registro')
                    print (pacientes)
                    input()
                else :
                    print('El DNI ingresado no esta en la base de datos')
                    input()


