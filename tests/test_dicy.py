import unittest
from dot.dicy import dicy


class test_dicy(unittest.TestCase):
    def test(self):
        d = dicy()
        with self.assertRaises(AttributeError):
            d.a
            
        d["a"] = 1
        self.assertEqual(d.a, 1)
        self.assertEqual(d["a"], 1)
        
        d.b = 2
        self.assertEqual(d.b, 2)
        self.assertEqual(d["b"], 2)
        
        
        del d.a
        with self.assertRaises(AttributeError):
            d.a

        del d.b
        with self.assertRaises(AttributeError):
            d.b
        

if __name__ == '__main__':
    unittest.main()
