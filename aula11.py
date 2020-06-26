# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:05:20 2020

@author: reis-
"""

import pymongo

# conexão com mongoDB
cliente = pymongo.MongoClient("localhost", 27017)
db = cliente.aula

albuns = db.albuns.find()

file = open("albuns.txt", "a")

for item in albuns:
    nome = item["nome"]
    file.write(nome + '\n')
    
file.close()