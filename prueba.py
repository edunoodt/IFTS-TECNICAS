def pri():
    print ('primera')

def seg():
    print ('Segunda')

def ter():
    print('Tercera')


lista = [pri, seg, ter]
opc = int(input ('====>>>> '))-1
lista[opc]()
