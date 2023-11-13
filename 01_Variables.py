# Buenas practicas de variables : first_name

# Variables
my_string = 'My String variable'
print(my_string)

my_int = 5
print(my_int)

my_float = 1.43
print(my_float)

my_bool = True
print(my_bool)


# Concatenacion de variables en un print
print(my_int, my_string)
print('Este es el valor de: ', my_bool)

# Algunas funciones del sistema
print(len(my_string))


# Variables en una sola linea. No abusar de esto!

name, surname, alias, age = 'Esdeath', 'San', 'Esdeath-Dev', 22

print('My name is:',name, surname +'. My age is: ',age, 'And my alias is: ',alias)


# Input
name = input('What is your nam: ')
age = input('How old are u: ')
print(name)
print(age)

# Cambiamos su tipo
name = 32
age = 'Esdeath'
print(name)
print(age)


# Forzamos el tipo?
address: str = "Mi direccion"
address = 32
address = True
address = 1.2

print(address)