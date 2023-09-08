from dot.ency import ency
from dot.dicy import dicy

class encyTest(ency):
    def __init__(self):
        self.dot1 = {"a": 1, "b": 2}
        self.dot2 = dicy({"c": 3, "e": 5, "f": dicy({"y": 6})})
        self.dot3 = {"d": 4, "e": 55, "f": {"z": 66}}
        self.e = 0.5
        self.f = {"x": 0.6}

        super().__init__(("dot1", "dot2", "dot3"))

    def selfTest(self, ut):
        '''Note that this test is self-destructive, it only works once'''
        ut.assertEqual(self.f, {'x': 0.6})
    
        self.f["x"] = 0.7
        ut.assertEqual(self.f, {'x': 0.7})
    
        del self.f
        ut.assertEqual(self.f, {'y': 6})
        ut.assertEqual(self.f.y, 6)
    
        self.f.y = 7
        ut.assertEqual(self.f, {'y': 7})
        ut.assertEqual(self.f.y, 7)
    
        del self.f
        ut.assertEqual(self.f, {'z': 66})
    
        self.f["z"] = 77
        ut.assertEqual(self.f, {'z': 77})
    
        del self.f
        with ut.assertRaises(AttributeError):
            self.f

class encyTestSimple(ency):
    def __init__(self):
        self.dot1 = {"a": 1, "b": 2}
        super().__init__(("dot1"))

    def selfTest(self, ut):
        ut.assertEqual(self.f, {'a': 1})
    
        ut.assertEqual(self.f, {'b': 2})

        self.f.c = 3
        ut.assertEqual(self.f, {'c': 3})

        del self.f.c
        with ut.assertRaises(AttributeError):
            self.f
