import unittest
from dot.dicy import dicy
from dot.ency import ency


class test_ency(unittest.TestCase):
    def test(self):
        
        class encyTest(ency):
            def __init__(self):
                self.dot1 = {"a": 1, "b": 2}
                self.dot2 = dicy({"c": 3, "e": 5, "f": dicy({"y": 6})})
                self.dot3 = {"d": 4, "e": 55, "f": {"z": 66}}
                self.e = 0.5
                self.f = {"x": 0.6}
                
                super().__init__(("dot1", "dot2", "dot3"))
        
        ef = encyTest()
        
        self.assertEqual(ef.f, {'x': 0.6})
        
        ef.f["x"] = 0.7
        self.assertEqual(ef.f, {'x': 0.7})
        
        del ef.f
        self.assertEqual(ef.f, {'y': 6})
        self.assertEqual(ef.f.y, 6)
        
        ef.f.y = 7
        self.assertEqual(ef.f, {'y': 7})
        self.assertEqual(ef.f.y, 7)
        
        del ef.f
        self.assertEqual(ef.f, {'z': 66})
        
        ef.f["z"] = 77
        self.assertEqual(ef.f, {'z': 77})
        
        del ef.f
        with self.assertRaises(AttributeError):
            ef.f
            

if __name__ == '__main__':
    unittest.main()
