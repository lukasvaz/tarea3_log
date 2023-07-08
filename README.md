# Estructuras
Las  estructuras necesarias estan implementadas en filter.py  y hashing.py.Se utiliza bitarray para implementar el filtro (Está especificado en requirements.txt)

# Test de correctitud
Estos tests tienen solo por fucnión verificar que las estructuras fueron implementadas correctamente.Para ejecutarlos:

correr tests de correctitud filtro:  python -m  unittest -v filter_tests

correr tests de correctitud hashing:  python -m  unittest -v  hashing_tests

# Test de funcionamiento
Todos Los resultados se encuentran en la carpeta "resultados".
Estos tests implementan los experimentos  mencionados  en el informe, para ejecutar:

Experimento 1 (Exploración):
ejecución: python experimento1.py

Experimento 2 (Comparacion m y k teoricos):

ejecución (para calculos teoricos): python experimento2_teoria.py
ejecución (para calculos empiricos): python experimento2_empirico.py

Eperimento 3 (Estimación de k):Para obtener los valores teóricos se hace uso del siguiente recurso: 
https://hur.st/bloomfilter/

ejecución (se debe imponer m ):python experimento3.py

Experimento 4 (Comparación de tiempos):
ejecución (se debe imponer el porcentaje  de busq infructuosas ):python experimento4.py

