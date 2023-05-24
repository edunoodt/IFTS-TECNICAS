from os import system
import platform


siso = platform.system()

print (siso)

match siso:
    case 'Windows':
        system ('cls')
        print ('Windows')
    case 'Linux':
        system('clear')
        print ('Linux')
    case _:
        print ('Otro sistema')

