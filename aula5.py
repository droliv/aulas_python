# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:15:07 2020

@author: reis-
"""


#condicionais

a = int(input('primeiro valor'))
b = int(input('segundo valor'))
c = int(input('terceiro valor'))


if(a > b and a > c):
    print('O maior valor é: {}'.format(a))
elif(b > a and b > c):
    print('O maior valor é: {}'.format(b))
else:
    print('O maior valor é: {}'.format(c))
    
