performance = []
for i in range (10):
    nota = float(input('\nIngrese la nota==>> '))
    
    if nota == 10 : 
        desempenio = 'LS'
    elif nota<10 and nota >= 8: 
        desempenio = 'LSat'
    elif nota < 8 and nota >= 6:
        desempenio = 'LB'
    else:
        desempenio = 'LNo'
    performance.append(desempenio)

print('\n',performance,'\n')





