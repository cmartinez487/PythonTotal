name = input('Usuario, dime tu nombre: ')
sales = input('y cuanto haz vendido este mes: ')
operation = (int(sales) * 13)/100

operation = round(operation, 2)

print(f'el vendedor {name} ha vendido un total de: {operation}')