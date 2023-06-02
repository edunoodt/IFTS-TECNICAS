"""
Indice de Masa Corporal

IMC = Peso/altura**2


    IMC     	CLASIFICACIÓN
<16.00          Infrapeso: Delgadez Severa
16.00 - 16.99   Infrapeso: Delgadez moderada
17.00 - 18.49   Infrapeso: Delgadez aceptable
18.50 - 24.99   Peso Normal
25.00 - 29.99   Sobrepeso
30.00 - 34.99   Obeso: Tipo I
35.00 - 40.00   Obeso: Tipo II
>40.00          Obeso: Tipo III

"""
from os import system
system('cls')


peso = float(input('Ingrese su peso en Kg:  '))
altura =float(input("Ingrese su altura en cm: "))

altura = altura/100

imc = peso/altura/altura

match imc:
    case n if n<16:
        print('su IMC es: ',imc,' => Infrapeso, Delgadez Extrema')
        print('Su peso ideal sería de ',18.5*altura*altura)
    case n if n<17:
        print('su IMC es: ',imc,' =>Infrapeso, Delgadez Moderada')
        print('Su peso ideal sería de ',18.5*altura*altura)
    case n if n<18.5:
        print('su IMC es: ',imc,' =>Infrapeso, Delgadez Aceptable')
        print('Su peso ideal sería de ',18.5*altura*altura)
    case n if n<25:
        print('su IMC es: ',imc,' =>Peso Normal')
    case n if n<30:
        print('Sobrepeso')
        print('su IMC es: ',imc,' =>Su peso ideal sería de ',25*altura*altura)
    case n if n<35:
        print('\nsu IMC es: //// {:.2f} \\\\\\\\ => OBESO Tipo I\n'.format(imc))
        print('Su peso ideal sería de ',25*altura*altura)
    case n if n<40:
        print('su IMC es: ',imc,' =>OBESO Tipo II')
        print('Su peso ideal sería de ',25*altura*altura)
    case n if n>40:
        print('su IMC es: ',imc,' =>OBESO Tipo III')
        print('Su peso ideal sería de ',25*altura*altura)