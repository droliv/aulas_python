# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:25:37 2020

@author: reis-
"""
import shutil

#escrita de arquivos

#valida se o arquivo existe, cria e sobscreve.
def criar_arquivo(arquivo, texto):
    arquivo = open(arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()
#valida se o arquivo existe, cria e estende
def atualizar_arquivo(arquivo, texto):
    arquivo = open(arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(arquivo):
    arquivo = open(arquivo, 'r')
    return arquivo.read()

#copiar arquivos
def copia_arquivo(arquivo, diretorio):
    shutil.copy(arquivo, diretorio)
    
#mover arquivos
def mode_arquivo(arquivo, diretorio):
    shutil.move(arquivo, diretorio)

criar_arquivo('teste.txt','10 7 5 9')

notas = ler_arquivo('teste.txt')
print(notas)
#calculo e media com lambda
notas = notas.split(' ')

media = lambda notas: sum([int(x) for x in notas])/len(notas)

print(media(notas))