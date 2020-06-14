# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:45:03 2020

@author: reis-
"""


class Television:
    def __init__(self):
        self.ligada = False
        
    def power(self):
        self.ligada = not self.ligada
        


tv = Television()
print(tv.ligada)
tv.power()
print(tv.ligada)