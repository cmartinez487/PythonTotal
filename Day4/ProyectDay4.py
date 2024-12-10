#Realizar un programa que le pregunte al usuario su nombre y un numero del 1 al 100
#1ero - el programa debe comparar el nro dado con uno random, solo se cuenta con 8 intentos - listo
#2do -  en cada intento el programa debe responder 4 cosas distintas
#2.1 - validacion 1, si el nro del usuario es menor a 1 y mayor a 100, debe dar un mensaje diciendole que el rango es hata 100
#2.2 - validacion 2, si el nro del usuario es menor al numero del programa, decir que la respuesta es incorrecta
#2.3 - validacion 3, si el nro del usuario es mayor al numero del programa, decir que la respuesta es incorrecta
#nota: las validaciones 2 y 3 se puede sinplificar con un or
#2.4 - validacion 4, si el usuario acierta el numero se le dice que gano, se le dice en cuantos intentos gano y se cierra el programa
# #

from random import randint

retries = 0
secretNumber = randint(1, 100)
name = str(input("Ingresa tu nombre:"))
#print(f'pista : {secretNumber}')

while retries <8:
    retries +=1
    userNumber = int(input("Ingresa un número (de preferencia del 1 al 100): "))
    if 1 <= userNumber <= 100: #tambien se puede if userNumber not in range(1,101):
        if userNumber < secretNumber or userNumber > secretNumber:
            print(f'{name} el numero {userNumber} no es el correcto... tienes {8 - retries} mas...')
        else:
            print(f'{name} el numero {userNumber} es el correcto!!! haz ganado en {retries}')
            break
    else:
        print(f'{name} el rango de numeros a ingresar es del 1 al 100, no acepto este numero {userNumber} como valido... tienes {8 - retries} mas...')
else:
    print(f'Haz usado tus 8 intentos para adivinar el nro que he pensado... gracias por intentarlo {name}')