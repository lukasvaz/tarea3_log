from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import time
#import pandas as pd


print("Pruebas insertarndo 93890 elementos y luego buscando 100 que no estan en la tabla")
print("Valores de k y resultados de falsos positivos:")
arr = []
m= 400000
print(f"M={m}")
k=3
cantN= 50
#res=0
i=0
j=0
babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")

for row in babies_file:
    if babies_file.line_num==1:continue
    print(row)
    while i < cantN:
        
        moneda= random.randint(0,1)

        if(moneda == 1):
            arr.append(row)
            print("agregando name")
            i +=1
    break

for row in films_file:
    while j < cantN:
        moneda= random.randint(0,1)
        if films_file.line_num==1:continue

        if(moneda == 1):
            arr.append(row)
            print("agregando film")
            j +=1
    break

#########################Sin Filtro###############################
inicioSF = time.time()
jaja= 0
correctas=0
for name in arr:

    for row in babies_file:
        #print(row[0])
        # Si el elemento existe, se imprime lo siguiente
        if name == row[0]:
            jaja +=1
            print(str(jaja))
            correctas+=1
            break

finalSF= time.time()

tiempo_totalSF = (finalSF - inicioSF)  * 1000

print(str(correctas))
print("el tiempo total de Sin filtro es "+str(tiempo_totalSF))
print()



########################Con Filtro##############################
tiempoi= time.time()


filter=BloomFilter(m,[Hashing(m).hash for j in range(0,k)])


def buscaDPSfiltro(name: str):
    for row in babies_file:
        #print(row[0])
        # Si el elemento existe, se imprime lo siguiente
        if name == row[0]:
            return 1
    return 0

for row in babies_file:
    #print(''.join(row))
    filter.add(''.join(row))
    

tiempoAnadido =  time.time()
tiempo_totalAnadido = (tiempoi - tiempoAnadido) * 1000
fp=0
for name in arr:
    #if babies_file.line_num==1002:break
    #print(''.join(row))
    resultado = filter.check(''.join(name))
    #print(resultado) 
    if resultado:
        if (buscaDPSfiltro(name) == 0):
            fp+=1
        

timepoF= time.time()

tiempo_total = (tiempoi - timepoF) * 1000

print("el tiempo total de añadido es "+str(tiempo_totalAnadido))
print("el tiempo total del filtro es "+str(tiempo_total))
print("cantidad FP: "+ str(fp))
########################################################################





