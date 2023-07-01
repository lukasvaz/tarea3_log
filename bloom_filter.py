from bitarray import bitarray
from collections.abc import Callable

# hash_array=list[function()]
class BloomFilter():
    '''Bloom Filter Class '''
    def __init__(self,filter_size:int,fun_array:list[Callable]):
        '''initializes a Bloom  filter, hash_k defines the number  
            of hash functions used in this instance and filter size defines the size  of M bits-array '''        
        self.size=filter_size
        self.bit_array= bitarray('0'*filter_size)
        self.fun_array=fun_array

    def  add(self,element:str):
        '''Appends an object  into  the filter.Iterates over  the list of functions and set to 1 every result in 
        bit array according the result of a particular function''' 
        if not  isinstance(element,str):raise TypeError("element is not str")     
        for f in self.fun_array:
            self.bit_array[f(element)]=1

    def check(self,element:str):
        '''Check if an element was added into the filter,returns a boolean.Its one sided, ie calculates the value of the
         requested element over the list of functions and  if any value is different to 1, then the element certainly was not added to the filter,
         if all values are 1,the element was probably added to the filter'''        
        for f in self.fun_array:
            if self.bit_array[f(element)]==0 :return False
        return True
    

    def get_bit_array(self):
        return self.bit_array
    def __str__(self):
        return str(self.bit_array)
    def __len__(self):
        return len(self.bit_array)
