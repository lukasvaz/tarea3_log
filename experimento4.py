from bloom_filter import BloomFilter
from hashing import Hashing
import random
import csv
import time

def buscaDPSfiltro(name: str, file):
    for i in range(len(file)):
        if file[i] == name:
            return 1
    return 0

    #for nombre in file:
    #    if name == nombre:
    #        return 1
    #return 0


porc = [0.75]
filename = "resultadosV1.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Tamaño Arreglo", "Tiempo Total sin Filtro", "Correctas sin Filtro",
                     "Tiempo Total del Filtro", "Cantidad FP", "Correctas"])

    for exponent in range(10, 17):
        arr_size = 2 ** exponent
        m = 585425
        k = 4
        babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        films_file = csv.reader(open('data/Film-Names.csv', "r", encoding="utf8"), delimiter=",")

        for i in range(len(porc)):
            print("TAMANO BUSQUEDA: {} | {} PELICULAS ".format(arr_size, porc[i]))

            numFilm = int(arr_size * porc[i])
            numNom = arr_size - numFilm
            arr = []

            def agregarNombres(arreglo: list, file):
                rowsName = list(file)
                random.shuffle(rowsName[1:])
                i = 0
                for row in rowsName[1:]:
                    moneda = random.randint(0, 1)
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

            babies_file2 = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
            babies_n = [row[0] for row in babies_file2]

            #########################Sin Filtro###############################
            print(" Busqueda sin filtro")
            inicioSF = time.time()
            correctas = 0
            for name in arr:
                for i in range(len(babies_n)):
                    if babies_n[i] == name:
                        correctas += 1
                        break 


                #if name in babies_n:
                #    correctas += 1
            finalSF = time.time()
            tiempo_totalSF = (finalSF - inicioSF) * 1000

            print("     Tiempo: " + str(tiempo_totalSF))
            print("     Correctas: " + str(correctas))

            ########################Con Filtro##############################
            print(" Busqueda con filtro")
            babies_file3 = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")
            babies = [row[0] for row in babies_file3]
            filter = BloomFilter(m, [Hashing(m).hash for _ in range(0, k)])

            for row in babies:
                filter.add(row)

            tiempobusFIL = time.time()

            fp = 0
            corr = 0
            for name in arr:
                if filter.check(name):
                    if buscaDPSfiltro(name, babies):
                        corr += 1
                    else:
                        fp += 1

            timepoF = time.time()
            tiempo_total = (timepoF - tiempobusFIL) * 1000

            print("     Tiempo: " + str(tiempo_total))
            print("     Cantidad FP: {} ".format(fp))
            print("     Correctas: {}".format(corr))

            # Escribir los resultados en el archivo CSV
            writer.writerow([arr_size, tiempo_totalSF, correctas, tiempo_total, fp, corr])
