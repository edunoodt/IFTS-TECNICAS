from os import system
import pickle
system('cls')

"""
texto = 'El patrimonio del cofundador de Nvidia, Jensen Huang, aumentó ayer jueves en más de USD 6.000 millones hasta alcanzar un máximo histórico, después de que el fabricante de chips pronosticara ventas que superan las expectativas, lo que disparó sus acciones.'

with open ('prueba\info.txt','w') as archi:
    archi.write(texto)


diccio = {'a': 'primera vocal', 'e': 'segunda vocal', 'i': 'tercera vocal', 'o': 'cuarta vocal', 'u': 'quinta vocal'}

with open ('prueba\midiccionario', 'wb') as midicti:
    pickle.dump(diccio,midicti)

"""
lista = ['Jirafa','Leon','Puma','Rinoceronte','vivora']

with open ('prueba\miarchivo', 'ab+') as file:
    pickle.dump(lista,file)

lista2 = ['papa','batata','poroto','banana']

with open ('prueba\miarchivo', 'ab+') as file:
    pickle.dump(lista2,file)




with open ('prueba\miarchivo','rb') as pepe:
    vocales = pickle.load(pepe)

print(vocales)
