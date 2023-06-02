from os import system
system ('cls')

moneda = ''

arg = float(input('Ingrese el tipo de cambio de argentina:  '))
chi = float(input('Ingrese el tipo de cambio de chile:  '))
bra = float(input('Ingrese el tipo de cambio de Brasil:  '))

while moneda != 'S':
    system('cls')
    print('Ingrese la primer letra de su moneda\n(A)rgentinos, (C)hilenos, ((R)eales),(S)alir')
    moneda = input().upper()
    
    if moneda != 'S':
        cant = float(input('Ingrese la cantidad ==>>  '))
        if moneda == 'A':
            dolar= cant/arg
        elif moneda == 'C':
            dolar = cant/chi
        elif moneda == 'R':
            dolar = cant/bra
        else:
            print ('No es una opción válida')
        print (dolar)
        input()


