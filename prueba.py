from os import system
system('cls')

def pri():
    print ('primera')

def seg():
    print ('Segunda')

def ter():
    print('Tercera')


lista = [pri, seg, ter]
opc = int(input ('Ingrese 1, 2 ó 3 ====>>>> '))-1

lista[opc]()
input('pulse enter para continuar')