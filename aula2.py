# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:12:03 2020

@author: reis-
"""


pets = ["Gato", "Cachorro", "Coelho"]

for pet in pets:
    print(pet)
    
#gerar numeros
for valor in range(1,5):
    print(valor)
    
#gerar uma lista de valores
numeros = list(range(1,5))
print(numeros)

quadrados = []
for num in range(1,11):
    quadrado = num ** 2
    quadrados.append(quadrado)

print(quadrados)

#funções estatisticas nativas

numeros = list(range(0,10))
print(min(numeros))
print(max(numeros))
print(sum(numeros))

#vai imprimir do 0 ao 5
print(numeros[0:6])

#imprimir a partir de um indice
print(numeros[1:])

#copiar uma lista

#a nova lista referencia o mesmo endereço de memória.
newList = numeros

#a nova lista referencia um novo endereço de memória
newList = numeros[:]































