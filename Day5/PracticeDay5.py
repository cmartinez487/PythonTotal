#ayuda contextual - buscar en la documentacion
"""
mensaje = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(mensaje.lstrip(',:%_#'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
print(marcas_smartphones.isdisjoint(marcas_tv))
"""

#funciones
'''
def greetUser(name):
    #definicion basica de una funcion
    print(f'Hola {name}')


nombre = input("cual es tu nombre? ")
greetUser(nombre)

#funciones con return

def greetUser(name):
    mensaje = 'Hola ' + name
    return mensaje

nombre = input("cual es tu nombre? ")
greetUsuario = greetUser(nombre)
print(greetUsuario)

def invertir_palabra(valor:str):
    return valor[::-1].upper()

palabra = 'Python'
print(invertir_palabra(palabra))
'''

#funciones con *args y *kwargs

'''
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1,2,3,4,5,6,7,8,9))

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")
        total+= valor

    return total

totalItems = suma(x=1, y=2, z=3)
print(totalItems)


def suma(num1, num2, *args, **kwargs):

    print(num1)
    print(num2)

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

#print(suma(1,2,1,2,3,4,5,6,7,8,9, x=10, y=101, z=202))

args = [1,2,3,4,5]
kwargs = {'alpha':101,'beta':202,'gamma':303}
print(suma(12,24, *args, **kwargs))
'''