from os import system

numero = ''

while numero != '*':
    system('cls')
    primo = True

    numero = input('Ingrese un numero entre 3 y 20\n o "*" para salir\nComo resultado se informara si es o no primo:  ')

    if numero !='*':
        numero = int(numero)
        while numero<3 or numero>20:
            print ('No ingreso un número dentro del trango correcto')
            numero = int(input('Ingrese un numero entre 3 y 20:  '))
        if numero % 2 == 0:
            limite = numero/2
        else:
            limite = numero //2+1
        indice = 2
        while indice <= limite:
            if numero % indice == 0:
                primo = False
                break
            indice +=1
        print('==================================')
        if primo:
            print ( str(numero) + ' Es numero primo')
        else:
            print ( str(numero) + ' no es numero primo')
        print('==================================')
        input('presione cualquier tecla para continuar')

    