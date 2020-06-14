# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:29:28 2020

@author: reis-
"""


#conjuntos

conjunto = {1,2,3,4,5,5,4}

#não vai imprimir os itens repetidos
print(conjunto)

# add item ao conjunto
conjunto.add(6)
print(conjunto)

# uniao de conjuntos
conjunto2 = {6,7,8}
print(conjunto.union(conjunto2))

#intersecção de conjuntos
print(conjunto.intersection(conjunto2))

#diferença entre conjuntos
print(conjunto.difference(conjunto2))

#verifica se um conjunto é subconjunto do outro
print(conjunto.issubset(conjunto2))

#verifica se um conjunto é superconjunto do outro
print(conjunto.issuperset(conjunto2))

#converter um array para conjunto (remove as duplicidades)

animais = ["gato", "gato", "cachorro", "coelho"]
animais = set(animais)
print(animais)
print(list(animais))