# Ingreso el valor máximo de la lista
limite = int(input('\n\ningrese un número 0>  '))

# Inicializo una lista vacía
lista =[]

# Voy agregando en la lista los valores de i, desde cero hasta el valor indicado
for i in range(limite+1): # El rango lo hago hasta el límite +1 para incluir el numero ingresado en la lista
    lista.append(i)

# Imprimo la lista
print ('\n',lista)

# Inicializo una variable en cero donde voy a sumar todos los valores
suma=0

# Recorro la lista y voy sumando los valores
for j in lista:
    suma+=j

# Imprimo la suma
print ('\n',suma,'\n','\n')
