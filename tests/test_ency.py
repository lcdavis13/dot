import pickle
import unittest
from dot.dicy import dicy
from dot.ency import ency
from .helper.encyTest import encyTest, encyTestSimple


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
            
    def test_readwriteSimple(self):

            ef = encyTestSimple()

            js = pickle.dumps(ef)
            ef2 = pickle.loads(js)

            self.assertEqual(ef2.dot1["a"], ef.dot1["a"])
            self.assertEqual(ef2.dot1["b"], ef.dot1["b"])

    # def test_readwrite(self):
    #
    #         ef = encyTest()
    #
    #         js = pickle.dumps(ef)
    #         ef2 = pickle.loads(js)
    #
    #         self.assertEqual(ef2.dot1["a"], ef.dot1["a"])
    #         self.assertEqual(ef2.dot1["b"], ef.dot1["b"])
    #         self.assertEqual(ef2.dot2["c"], ef.dot2["c"])
    #         self.assertEqual(ef2.dot2["e"], ef.dot2["e"])
    #         self.assertEqual(ef2.dot2["f"]["y"], ef.dot2["f"]["y"])
    #         self.assertEqual(ef2.dot3["d"], ef.dot3["d"])
    #         self.assertEqual(ef2.dot3["e"], ef.dot3["e"])
    #         self.assertEqual(ef2.dot3["f"]["z"], ef.dot3["f"]["z"])


if __name__ == '__main__':
    unittest.main()
