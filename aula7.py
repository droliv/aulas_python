# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:25:33 2020

@author: reis-
"""


#Classes, funções e metodos

# método - def

class Calculadora:
# =============================================================================
#     def __init__(self, n1, n2):
#         self.a = n1
#         self.b = n2
# =============================================================================
    
    def soma(self, a, b):
        return a + b
    

calculadora = Calculadora()
print(calculadora.soma(3,4))
