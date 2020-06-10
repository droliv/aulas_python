# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import math

"""
print("Hello World")

num1 = 10

print ("O primeiro numero é ".upper() + str(num1))

nome = input("Digite seu nome: ")
print("Olá " + nome)

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro numero: "))

print("A soma dos números é: "+ str(num1 + num2))
print("a potência do primeiro número é: " + str(num1**2))
print("a raiz quadrada do segundo número é: " + str(math.sqrt(num2)))
"""

pets = ["gato", "Cachorro", "Peixe"]
#insere ao final do array
pets.append("Coelho")
#insere em posicao específica
pets.insert(1, "hamster")
print(pets)

#remove elemento especifico
del pets[0]
#remove ultimo elemento
pets.pop()
#remove em posocao especifica
pets.pop(1)
#remove pelo valor
pets.remove("Peixe")
print(pets)
pets = ["Gato", "Cachorro", "Peixe"]

#ordena array de forma ascendente
pets.sort()
print(pets)
#ordena array de forma descendente
pets.reverse()
print(pets)
#tamanho do array
print(len(pets))