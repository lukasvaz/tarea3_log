import math

def opt_m(n,p,k):
  m= (-1)*(n * math.log(p)) / (math.log(2) ** 2)
  m= round(m)
  return m


def opt_k1(p):
    k = - (math.log(p) / math.log(2))
    k = round(k)
    return k

def opt_k2(n, p, m):
    k = (m / n) * math.log(1 / p)
    k = round(k)
    return k

n = 93890
p = 0.01
k1 = opt_k1(p)
m = opt_m(n,p,k1)#104857
k2 = opt_k2(n, p, m)



print("Valor óptimo de k1:", k1)
print("Valor óptimo de m:", m)
print("Valor óptimo de k2:", k2)