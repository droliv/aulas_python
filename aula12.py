# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:10:20 2020

@author: reis-
"""


from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="nosql")

#create some nodes with labels

user = db.labels.create("Usuario")

u1 = db.nodes.create(name="Bob")
u2 = db.nodes.create(name="Alice")

user.add(u1, u2)

u1.relationships.create("follows", u2)