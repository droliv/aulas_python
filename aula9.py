# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:57:18 2020

@author: reis-
"""

# importação de modulos
from aula8 import Television


television = Television()
television.power()
print(television.ligada)


#funções anônimas lambda

contador_letras = lambda lista: [len(x) for x in lista]

lista_pets = ['cachorro', 'gato', 'coelho']

print(contador_letras(lista_pets))


soma = lambda a, b: a + b

print(soma(2,9))


#dicionario lambdas

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
    
}

soma = calculadora['soma']
print(soma(3,56))

























