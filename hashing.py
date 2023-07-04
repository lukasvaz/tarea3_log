import random

class Hashing:

    # Inicia los valore del hashing, requiere el tamaño de la tabla size_m
    def __init__(self, size_m:int):
        self.m = size_m                         # Se guarda el valor de size_m en m
        self.P = self.primo()                   # Se busca un numero primo mayor a m
        self.a = []                             # Se crea un arreglo vacio en el que se guardaran los valores de a
        self.b = random.randint(0, self.P-1)    # Se crea un valor aleatorio que se guardara en b

    # Retorna el proximo numero primo mayor a n
    def primo(self):
        archivo = open("primos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            if ( int(linea) > self.m ):
                return int(linea)
        return None 
    
    def primo(self):

        def es_primo(numero):
            if numero < 2:
                return False
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    return False
            return True
        
        primo = self.m +1
        while not es_primo(primo):
            primo += 1
            return primo
    
    def hash(self, word : str):
        # Se crean nuevos valores en a si el largo de word es mayor a los elementos en a
        for i in range(0, len(word) - len(self.a) ):
            self.a.append(random.randint(1, self.P-1))
        
        # Se calcula la sumatoria de cada letra en x multiplicado por el valor en a correspondiente
        c = 0
        for i in range(0, len(word)):
            c += ((ord(word[i]) - 96) * self.a[i])

        # Se retorna el valor al aplicarle el hash
        return (((self.b + c) % self.P) % self.m )

    # Printea los valores guardados en el hashing
    def print(self):
        print(self.m, self.P, self.a, self.b)


