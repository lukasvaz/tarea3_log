from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import pandas as pd


m =2**20
k_interval = m//10
valores_k = []
resultados = []
k=1
while k < m:
    k*=2
    babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
    films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")
    filter=BloomFilter(m,[Hashing(m).hash for j in range(0,k)])
    valores = 0
    for row in babies_file:
        if babies_file.line_num==1:continue
        #if babies_file.line_num==100:break
        #print(''.join(row))
        filter.add(''.join(row))
    for row in films_file:
            if films_file.line_num==1:continue
            #if films_file.line_num==100:break
            #print(''.join(row))
            resultado = filter.check(''.join(row))
            #print(resultado) 
            if resultado:
                valores+=1
    print(k,valores)
    valores_k.append(k)
    resultados.append(valores)

print(m)
print(valores_k)
print(resultados)


