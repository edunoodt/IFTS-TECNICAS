from os import system
system ('cls')

with open ('Establecimientos_salud.txt','r') as arca:
    lista = arca.read()
    print (lista)