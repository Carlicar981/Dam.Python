a = 5
b = 10
c = 15

# Operador and
print(a > b and a > c )

# Operador or
print(a < b or a < c)

# Operador not
print(not (a < b or a < c))

lista = [1,2,3,4,5]
print(lista)
print(lista[0])
lista[0]=lista[0]+lista[4]
lista[1]=lista[1]+lista[3]

print(lista)
lista.append(10)

print(lista)
lista.remove(lista[5])
print(lista)
sublista = lista[1:3]

print(sublista)
from random import *
print(randint(0,10))