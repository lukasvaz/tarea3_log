from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import pandas as pd

# Experimento utilizando la calculadora de filtro bloom

print("===============================================")
print("- EXPERIMENTO UTILIZANDO CALCULADORA BLOOM -")
print()

e_b = 1000
e_i = 93000
print("Elementos a insertar: Todos")
print(f"Elementos a buscar: {e_b}")
#m = 134171
#k = 1
#print(f"Valor de m: {m} valor de k: {k}")
probabilidad_total = []
for i in range(0,5):
    for j in range(2,40):
        m = 2**j
        print()
        print(f"M: {m}")
        valores_k = []
        resultados = []
        for k in range(1,11):
            #print("----------------------------------------------")
            #print(f"Intento: {i+1}")
            #print(f"Valor de m: {m} valor de k: {k}")
            babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
            films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")
            filter=BloomFilter(m,[Hashing(m).hash for j in range(0,k)])

            #print("Insertando ->")
            falsos_positivos = 0
            for row in babies_file:
                if babies_file.line_num==1:continue
                #if babies_file.line_num==100:break
                #print(''.join(row))
                filter.add(''.join(row))
            #print("Buscando ->")
            for row in films_file:
                    if films_file.line_num==1:continue
                    if films_file.line_num==1002:break
                    #print(''.join(row))
                    resultado = filter.check(''.join(row))
                    #print(resultado) 
                    if resultado:
                        falsos_positivos += 1

            valores_k.append(k)
            resultados.append(falsos_positivos)
        print(valores_k)
        print(resultados)
        """
            print(f"falsos positivos: {falsos_positivos}")
            probabilidad_parcial = falsos_positivos/e_b
            probabilidad_total.append(probabilidad_parcial)
            print(f"Probabilidad: {probabilidad_parcial}")
         """
    print("----------------------------------------------")
"""
print("----------------------------------------------")

c = 0
for i in probabilidad_total:
     c+=i

promedio = c/len(probabilidad_total)
print(f"Promedio de probabilidad: {promedio}")

"""
print("===============================================")
