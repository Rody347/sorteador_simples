# This Python file uses the following encoding: utf-8
import os, sys
import random


#Escolha do tamanho do sorteio
n = input('Digite a quantidade de clientes a serem sorteados: ')


#Criando a amostragem:
a = []
for i in range(0,n):
     a.append(i + 1)
#Teste de variável:
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