from os import system

servicios={
    'Pediatria':[0,0],
    'Maternidad':[0,0],
    'Otros':[0,0]

}

texto="""Ingrese la operación que desea realizar
1.- Actualizar los montos del servicio
2.- Eliminar el servicio
3.- Ver el servicio
***.- Salir\n"""

opcion = ''

while opcion != '***':
    system('clear')
    opcion = input (texto)
    if opcion != '***':
        opcion = int (opcion)
        match opcion:
            case 1:
                servicio = input('Ingrese el servicio para actualizar, (M)aternidad, (P)ediatria, (O)tros:\n').upper()
                os = float(input('Ingrese el costo por obra social: '))
                part = float(input('Ingrese el costo en forma privada: '))

                match servicio:
                    case 'M':
                        servicios['Maternidad'][0]=os
                        servicios['Maternidad'][1]=part
                    case 'P':
                        servicios['Pediatria'][0]=os
                        servicios['Pediatria'][1]=part
                    case 'O':
                        servicios['Otros'][0]=os
                        servicios['Pediatria'][1]=part
                    case other:
                        print ('No es una opcion valida')
                        input()
                print (servicios)
            case 2:
                servicio = input('Ingrese el servicio que desea eliminar, (M)aternidad, (P)ediatria, (O)tros:\n  ').upper()
                match servicio:
                    case 'M': del servicios['Maternidad']
                    case 'P': del servicios['Pediatria']
                    case 'O': del servicios['Otros']
                    case other:
                        print ('No es una opcion Válida')
                        input()
            case 3:
                for clave, valor in servicios.items():
                    print ('Servicio {} : Costo {}'.format(clave,valor))
                input()
                




                

            
                    
                        
