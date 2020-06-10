# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:33:34 2020

@author: reis-
"""

#leitura de arquivos
arquivo = open('pessoas.txt', 'r')
for linha in arquivo:
    lista = linha.split()
    print(lista)
    
arquivo.close()

#escrita em arquivos
pets = ["Gato", "Cachorro", "Coelho"]

arquivo = open('pets.txt', 'w')
for pet in pets:
    arquivo.write(pet + '\n')

arquivo.close()