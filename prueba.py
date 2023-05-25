def pri():
    print ('primera')

def seg():
    print ('Segunda')

def ter():
    print('Tercera')


lista = [pri, seg, ter]
opc = int(input ('====>>>> '))-1
lista[opc]()


#[pri, seg, ter][opc]()


#cuenta = lambda x,y,z : (x *(1+ y))**(1/z)
#print (cuenta (6.2,0.3,3))

