from bloom_filter import BloomFilter
import random
import csv

filter=BloomFilter(2**20,[lambda x:ord(x[0]),lambda x:ord(x[1])])
#read csv, and split on "," the line
babies_file = csv.reader(open('data/Popular-Baby-Names-Final.csv', "r"), delimiter=",")

#loop through the csv list
print('Adding..')
for row in babies_file:
    if babies_file.line_num==1:continue
    if babies_file.line_num==8:break
    print(''.join(row))
    filter.add(''.join(row))
while True:
    name = input('¿Qué nombre desea buscar?\n')
    if name=='exit()':break
    print(filter.check(name))    

