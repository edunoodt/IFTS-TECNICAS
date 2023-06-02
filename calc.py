from os import system

system('cls')

def suma (a,b):
    return a+b

def resta (a,b):
    return a-b

def mult (a,b):
    return a*b

def div (a,b):
    return a/b
r=0
oper = ' '
while oper != 'x':
    print ('Ingrese la primer letra de operación deseada:','\n','(s)umar, (r)estar, (m)ultiplicar, (d)ividir, (x)salir')
    oper = input ('==>>  ')
    if oper != 'x':
        x = input('ingrese x (o "r" para usar el resultado anterior:  ')
        y = input('ingrese y (o "r" para usar el resultado anterior:  ')
        if x == 'r':
            x = r
        else:
            x = int(x)
        if y == 'r':
            y=r
        else:
            y = int (y)
        
        match oper:
            case 's':
                r = suma(x,y)
                system ('cls')
                print (x,' + ',y , ' = ', r)
            case 'r':
                r = resta(x,y)
                system ('cls')
                print (x,' - ',y , ' = ', r)
            case 'm':
                r = mult(x,y)
                system ('cls')
                print (x,' * ',y , ' = ', r)
            case 'd':
                r = div(x,y)
                system ('cls')
                print (x,' / ',y , ' = ', r)
