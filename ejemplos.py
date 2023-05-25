"""coins = ["Bitcoin", "Ethereum", "Cardano"]
prices = [48000,2585,2]
for i, coin in enumerate(coins):
    price = prices[i]
    print(f"{i+1}.- ${price} for 1 {coin}")
print('***********************************\n\n')

dict1 = {1: "Bitcoin", 2: "Ethereum"}
for key, value in dict1.items():
    print(f"Key {key} has value {value}")
"""

dict2 = {12472451:['Jorge','Gomez'], 36784512:['Daniel','Gutierrez'],25896541:['Juan','Perez']}
texto2=''
for clave,contenido in dict2.items():
     texto1 = (str(clave)+ ';' + contenido[0] + ';' + contenido[1]+'\n')
     texto2 = texto2+texto1

texto = 'los leones del africa son vegetarianos\nPero de cualquier modo, no me acercaria demasiado\n'

with open('prueba/archivo.txt','w') as archi:
        
        archi.write(texto2)
        #archi.write(texto)

print ('*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*')
dicti = {}
with open('prueba/archivo.txt','r') as archi:
     salida = archi.readline()
     while salida != '':
        claveb = True
        clave = ''
        lista = []
        palabra = ''
        for letra in salida:
            if letra != ';' and letra != '\n':
                palabra = palabra + letra
            elif claveb:
                clave = palabra
                claveb = False
                palabra =''
            else:
                 lista.append(palabra)
                 palabra = ''
        dicti[clave]=lista
        salida = archi.readline()
print (dicti)