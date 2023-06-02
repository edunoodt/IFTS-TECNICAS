from os import system
system('cls')


"""dicci = {'a':'primer letra','b':'segunda letra'}

print (dicci)
print (dicci['a'])
print (list(dicci.keys())[0])
print (dicci.values())
dicci['c']='tercera letra'
print (len(dicci))"""

#Funcion de ingreso de los coeficientes de la variable
def ingresoCoef():
    print('INgrese los coefecientes de las variables')
    matriz = []
    for i in range (3):
        fila = []
        for j in range (3):
            linea = i + 1
            col = j +1
            a = float(input('ingrese el coeficente{}-{} => '.format(linea,col)))
            fila.append(a)
        matriz.append(fila)
    return matriz

#Funcion de ingreso de los terminos independientes    
def ingresoTind():
    print ('Ingreso de los terminos independientes')
    tind=[]
    for i in range (3):
        fila = i+1
        tind.append(float(input('Ingrese termino {} => '.format(fila))))
    return tind

def muestraMatriz(q):
    for fila in range(3):
            print(' {:10.2f}{:10.2f}{:10.2f} '.format(q[fila][0],q[fila][1],q[fila][2]))

#Fubción para resolver el determinante de una matriz de 3x3
def resol(q):
    diagI01 = q[0][0]*q[1][1]*q[2][2]
    diagI02 = q[1][0]*q[2][1]*q[0][2]
    diagI03 = q[0][1]*q[1][2]*q[2][0]
    diagD01 = q[0][2]*q[1][1]*q[2][0]
    diagD02 = q[1][2]*q[2][1]*q[0][0]
    diagD03 = q[0][1]*q[1][0]*q[2][2]
    print (diagI01,diagI02,diagI03,diagD01,diagD02,diagD03)
    det = diagI01+diagI02+diagI03-diagD01-diagD02-diagD03
    print (det)
    return det

# ingreso de los términos independientes:
mtz = ingresoCoef()

muestraMatriz(mtz)

input()

#Ingreso de los términos independientes:
tind= ingresoTind()

#Calculo del determinante principal:
det = resol(mtz)
print (det)

#reemplazo coeficientes de x por los términos independientes:
mtzx = mtz
mtzx[0][0] = tind[0]
mtzx[1][0] = tind[1]
mtzx[2][0] = tind[2]

muestraMatriz(mtzx)
input()