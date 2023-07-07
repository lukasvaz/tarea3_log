from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import pandas as pd


print("Pruebas insertarndo 1000 elementos y luego buscando 1000 que no estan en la tabla")
print("Valores de k y resultados de falsos positivos:")
for j in range(10,21):
    m = 2**j
    print(f"M = { m }")
    valores_k = []
    resultados = []
    k = 1
    while k < m//64:
        k*=2
        babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")
        filter=BloomFilter(m,[Hashing(m).hash for j in range(0,k)])
        valores = 0
        for row in babies_file:
            if babies_file.line_num==1:continue
            if babies_file.line_num==1002:break
            #print(''.join(row))
            filter.add(''.join(row))
        for row in films_file:
                if films_file.line_num==1:continue
                if films_file.line_num==1002:break
                #print(''.join(row))
                resultado = filter.check(''.join(row))
                #print(resultado) 
                if resultado:
                    valores+=1
        valores_k.append(k)
        resultados.append(valores)
    
    print(valores_k)
    print(resultados)
