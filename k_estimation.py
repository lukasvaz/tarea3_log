from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import pandas as pd
import numpy as np 

m = 800000 #fijamos m
N=100000 #size tabla  nombres
print("Pruebas encontrando  un k optimo para cierto M fijo")
search_size=1000
resultados=[]
for k in range(1,20):
    # print(f"k = { k }")
    false_positive=0
    filter=BloomFilter(m,[Hashing(m).hash for j in range(0,k)])
    
    #anadiendo  nombres en el filtro con k variable 
    print("Anadiendo  nombres  en el filtro para k ={}".format(k))

    babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
    for row in babies_file:
        if babies_file.line_num==1:continue
        # print(row)
        filter.add(''.join(row))
        
    #generamos arreglo de busqueda ,solo elementos que  no fueron anadidos
    # para  estimar  la probabilidad  de  falso positivo
    print("Generamos arreglo de busqueda de 500 elementos no anadidos")
    search_keys=np.random.randint(1,3809,search_size)
    search_array=[]
    films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")    
    for row in films_file:
            if films_file.line_num==1:continue
            if films_file.line_num in search_keys :
                search_array.append(''.join(row))
                # print(search_array)

    #busqueda  de  elementos
    for movie in search_array:
         if(filter.check(movie)):false_positive+=1
    resultados.append(false_positive/search_size)
    print(resultados)