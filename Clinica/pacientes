import soporte as so


menu = """
1.- Modificación Datos del paciente
2.- Muestra datos del paciente
3.- Baja de un paciente
====>>> 
"""

pacientes = so.inicializaPac()
dni = ''

while dni != '***':
    so.borra()
    dni = so.ingresoDNI()

    if dni != 'error' and dni != '***':
        if not(so.verificaDNI(dni,pacientes)):
            resp = input('EL PACIENTE NO SE ENCUENTRA EN LA BASE DE DATOS.\n¿Quiere darlo de alta? S/N:  ').upper()
            if resp == 'S':
                pacientes = so.altaDNI(dni,pacientes)
        else:
            print('Indique la opcion buscada:')
            resp = input(menu)
    print (pacientes)





