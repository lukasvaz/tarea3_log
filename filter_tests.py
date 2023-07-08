from bloom_filter import BloomFilter


from bitarray import bitarray
import unittest


class AddTests(unittest.TestCase):
    def test_type_error(self):
        filter=BloomFilter(10,[lambda x: int(x)])
        with self.assertRaises(TypeError):
            filter.add(5)

    def test_common_case(self):
        filter=BloomFilter(10,[lambda x: int(x),lambda x: int(x)+1])
        self.assertEqual(filter.get_bit_array(),bitarray("0000000000"))
        filter.add('5')
        #default function returns x 
        self.assertEqual(filter.get_bit_array(),bitarray("0000011000"))

    def test_strfunction(self):
        filter=BloomFilter(10,[lambda x: ord(x[0])%97])
        filter.add("ala")
        self.assertEqual(filter.get_bit_array(),bitarray("1000000000"))
        filter.add("gato")
        self.assertEqual(filter.get_bit_array(),bitarray("1000001000"))

    def test_border(self):
        filter=BloomFilter(10,[lambda x: int(x)])
        # out of bound raises an arror
        with self.assertRaises(IndexError):
            filter.add('100')
            filter.add('-1')
        

class CheckTests(unittest.TestCase):
    def test_cases(self):
        filter=BloomFilter(10,[lambda x: ord(x[0])%97])
        #true positive
        filter.add("ala")
        self.assertTrue(filter.check('ala'))
        #true positive
        filter.add("gato")
        self.assertTrue(filter.check('gato'))
        #false positive
        self.assertTrue(filter.check('gafas'))
        #true negative
        self.assertFalse(filter.check('hola'))
        

        
if __name__=='__main__':
    unittest.main()