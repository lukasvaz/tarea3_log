from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import time

def buscaDPSfiltro(name: str, file):
    for nombre in file:
        if name == nombre:
            return 1
    return 0

porc = [0.25, 0.5, 0.75]

print("Pruebas insertando 93890 elementos y luego buscando 100 que no están en la tabla")
print("Valores de k y resultados de falsos positivos:")
for exponent in range(12, 15):
    arr_size = 2 ** exponent
    m = 585425
    k = 4
    babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
    films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")

    for i in range(len(porc)):
        numFilm = int(arr_size * porc[i])
        print("cant pelis: " + str(numFilm))
        numNom = arr_size - numFilm
        print("cant nombres: " + str(numNom))
        arr = []

        def agregarNombres(arreglo: list, file):
            rowsName = list(file)
            random.shuffle(rowsName[1:])
            i = 0
            for row in rowsName[1:]:
                moneda = random.randint(0, 1)
                nombre_name = row[0].replace(";", "")
                if moneda == 1:
                    arreglo.append(row[0])
                    i += 1

                if i >= numNom:
                    break

        def agregarPeli(arreglo: list, file):
            rowsFilm = list(file)
            random.shuffle(rowsFilm[1:])
            i = 0
            for row in rowsFilm[1:]:
                moneda = random.randint(0, 1)
                nombre_pelicula = row[0].replace(";", "")
                if moneda == 1:
                    arreglo.append(nombre_pelicula)
                    i += 1

                if i >= numFilm:
                    break

        agregarNombres(arr, babies_file)
        agregarPeli(arr, films_file)
        random.shuffle(arr)
        print("tamano arreglo: " + str(len(arr)))

        babies_file2 = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        babies_n = [row[0] for row in babies_file2]

        #########################Sin Filtro###############################
        inicioSF = time.time()
        correctas = 0
        for name in arr:
            if name in babies_n:
                correctas += 1
        finalSF = time.time()
        tiempo_totalSF = (finalSF - inicioSF) * 1000

        print("Cantidad correcta sin filtro: " + str(correctas))
        print("Tiempo total sin filtro: " + str(tiempo_totalSF))

        print()

        ########################Con Filtro##############################
        babies_file3 = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        babies = [row[0] for row in babies_file3]
        filter = BloomFilter(m, [Hashing(m).hash for _ in range(0, k)])

        tiempoi = time.time()
        for row in babies:
            filter.add(row)

        tiempoAnadido = time.time()
        tiempo_totalAnadido = (tiempoAnadido - tiempoi) * 1000
        fp = 0
        corr = 0

        tiempobusFIL = time.time()
        for name in arr:
            resultado = filter.check(name)
            if resultado:
                num = buscaDPSfiltro(name, babies)
                if num == 0:
                    fp += 1
                elif num == 1:
                    corr += 1

        timepoF = time.time()
        tiempo_total = (timepoF - tiempobusFIL) * 1000

        print("Tiempo total de añadido: " + str(tiempo_totalAnadido))
        print("Tiempo total del filtro: " + str(tiempo_total))
        print("Cantidad FP: " + str(fp))
        print("Cantidad correcta: " + str(corr))
        print("/\/\/\/\/")
    print("OTRO")
