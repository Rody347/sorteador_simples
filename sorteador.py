# This Python file uses the following encoding: utf-8
import os, sys
import random


#Criando a amostragem:
a = []
#n = input("Digite a quantidade de clientes será sorteado: ")
for i in range(0,10):
     a.append(i + 1)
print(a)


#Limitando o intervalo do número aleatório
t = len(a)


#Gerando número aleatório
s = random.randrange(1,t)

#Acessando e selecionando o número sorteado
x = a.index(s)
print('Indice sorteado: ')
print(x)
print("Elemento sorteado: ")
print(a[x])