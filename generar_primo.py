def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def obtener_primo_mayor(valor):
    primo = valor + 1
    while not es_primo(primo):
        primo += 1
    return primo

# Ejemplo de uso

for i in range(2,20):
    print(obtener_primo_mayor(i))

999979
print(obtener_primo_mayor(999979))