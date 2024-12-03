nombre = "Char"
#print(nombre)

nombre:str = 'Amuro'
#print(nombre)

#variables
num1 = 1
num2 = 2

#name = input('Usuario, dime tu nombre: ')
#lastName = input('y tu apellido: ')

#suma:int = num1 + num2

#print(name+" "+lastName, suma)

#integer y Floats - Conversion de datos
#comentar varias lineas...
'''
number = 1
print(number)
print(type(number))
print(number+number)

number = 5.8
print(number)
print(type(number))
print(number+number)

#conversion de float a int
number = int(number)
print(number)
print(type(number))
print(number+number)

number = 5 + 5.8
print(number)
print(type(number))
'''

'''
edad = input('dime tu edad: ')
print('tu edad es: '+ edad)

#conversion de string a int
nuevaEdad = int(edad)+1

conversion de str a int
print('tu nueva edad es: ' + str(nuevaEdad))


#Formatear Cadenas
#metodo 1
print('tu nueva edad es: {}'.format(nuevaEdad))

#metodo 2
print(f'tu nueva edad es: {nuevaEdad}')
'''
#operaciones Matematicas Basicas - Redondeo de numeros
num1 = 6
num2 = 2
num3 = 7

operacion = num1 + num2
print(f'suma: {operacion}')

operacion = num1 - num2
print(f'resta: {operacion}')

operacion = num1 * num2
print(f'multiplicacion: {operacion}')

operacion = num3 / num2
print(f'division: {operacion}')

operacion = num3//num2
print(f'division al pizo de {num3} entre {num2}: {operacion}')

operacion = num3%num2
print(f'{num3} modulo de {num2} y: {operacion}')

operacion = num1**num2
print(f'{num1} elevado a la {num2} y: {operacion}')

operacion = num1**3
print(f'{num1} elevado a la {3} y: {operacion}')

operacion = num1**0.5
print(f'Raiz cuadrada de {num1}: {operacion}')
#aplicamos redondeo

operacion = round(operacion, 2)
print(f'Raiz cuadrada de {num1}: {operacion} aplicando redondeo')