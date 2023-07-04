from bloom_filter import BloomFilter
import random
import csv
from hashing  import Hashing

# NAMES_SIZE=

m_bits=2**10
k_hashing=7
hashing_array=[]

for i in range(k_hashing):
    hashing=Hashing(m_bits)
    hashing_array.append(hashing)


filter=BloomFilter(m_bits,[fun.hash for fun in hashing_array])
#read csv, and split on "," the line
babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")

#loop through the csv list
print('Adding..')
for row in babies_file:
    if babies_file.line_num==1:continue

    # if babies_file.line_num==200:break

    print(''.join(row))
    filter.add(''.join(row))


print(filter)
while True:
    name = input('¿Qué nombre desea buscar?\n')
    if name=='exit()':break
    print(filter.check(name))    

