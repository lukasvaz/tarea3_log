from bloom_filter import BloomFilter
from hashing import Hashing
from bitarray import bitarray
import unittest

class HashingTests(unittest.TestCase):
    
    def test_constructor(self):
        hashing1 = Hashing(999)
        hashing2 = hashing1
        hashing3 = Hashing(999)
        self.assertEqual(hashing1.get(), hashing2.get())
        self.assertFalse(hashing1.get() == hashing3.get())

        hashing1 = Hashing(999)
        hashing2 = hashing1
        hashing3 = Hashing(999)
        self.assertEqual(hashing1.get(), hashing2.get())
        self.assertFalse(hashing1.get() == hashing3.get())

        hashing1 = Hashing(999)
        hashing2 = hashing1
        hashing3 = Hashing(999)
        self.assertEqual(hashing1.get(), hashing2.get())
        self.assertFalse(hashing1.get() == hashing3.get())

    def test_hash(self):
        hashing1 = Hashing(999)
        hashing2 = Hashing(999)
        word1 = "MARIANA"
        word2 = "ISIDORA"
        word3 = "ANTONIA"

        self.assertEqual(hashing1.hash(word1), hashing1.hash(word1))
        self.assertEqual(hashing2.hash(word1), hashing2.hash(word1))
        self.assertEqual(hashing1.hash(word2), hashing1.hash(word2))
        self.assertEqual(hashing2.hash(word2), hashing2.hash(word2))
        self.assertEqual(hashing1.hash(word3), hashing1.hash(word3))
        self.assertEqual(hashing2.hash(word3), hashing2.hash(word3))

        self.assertFalse(hashing1.hash(word1) == hashing1.hash(word2)) 
        self.assertFalse(hashing1.hash(word1) == hashing1.hash(word3)) 

        self.assertFalse(hashing1.hash(word1) == hashing2.hash(word1)) 
        self.assertFalse(hashing1.hash(word1) == hashing2.hash(word1)) 


        
if __name__=='__main__':
    unittest.main()