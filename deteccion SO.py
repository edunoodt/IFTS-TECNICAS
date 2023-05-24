from os import system
import platform
siso = platform.system()
match siso:
    case 'Windows':
        system ('cls')
    case 'Linux':
        system('clear')
    case _:
        print ('Otro sistema')

