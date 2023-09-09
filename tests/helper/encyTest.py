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
        
        #original state test
        ut.assertEqual(self.a, 1)
        ut.assertEqual(self.b, 2)
        ut.assertEqual(self.c, 3)
        ut.assertEqual(self.d, 4)
        ut.assertEqual(self.e, 0.5)
        ut.assertEqual(self.f, {"x":0.6})
        ut.assertEqual(self.f["x"], 0.6)
        ut.assertEqual(self.dot2.e, 5)
        ut.assertEqual(self.dot2.f, {"y":6})
        ut.assertEqual(self.dot2.f.y, 6)
        ut.assertEqual(self.dot3["e"], 55)
        ut.assertEqual(self.dot3["f"], {"z":66})
        ut.assertEqual(self.dot3["f"]["z"], 66)
        
        
        #INSERTION TEST
        
        #insert to class by default
        self.w = 0.7
        ut.assertEqual(self.w, 0.7)
        ut.assertEqual(self.__dict__["w"], 0.7)
        with ut.assertRaises(KeyError):
            self.dot1["w"]
        with ut.assertRaises(AttributeError):
            self.dot2.w
        with ut.assertRaises(KeyError):
            self.dot3["w"]
        #delete
        del self.w
        with ut.assertRaises(AttributeError):
            self.w

        # insert to first dict
        self.dot1["w"] = 7
        ut.assertEqual(self.w, 7)
        with ut.assertRaises(KeyError):
            self.__dict__["w"]
        with ut.assertRaises(AttributeError):
            self.dot2.w
        with ut.assertRaises(KeyError):
            self.dot3["w"]
        #delete
        del self.w
        with ut.assertRaises(AttributeError):
            self.w

        # insert to second dict (a dicy)
        self.dot2.w = 70
        ut.assertEqual(self.w, 70)
        with ut.assertRaises(KeyError):
            self.__dict__["w"]
        with ut.assertRaises(KeyError):
            self.dot1["w"]
        with ut.assertRaises(KeyError):
            self.dot3["w"]
        #delete
        del self.w
        with ut.assertRaises(AttributeError):
            self.w

        # insert to third dict
        self.dot3["w"] = 700
        ut.assertEqual(self.w, 700)
        with ut.assertRaises(KeyError):
            self.__dict__["w"]
        with ut.assertRaises(KeyError):
            self.dot1["w"]
        with ut.assertRaises(AttributeError):
            self.dot2.w
        #delete
        del self.w
        with ut.assertRaises(AttributeError):
            self.w
            
        
        #TODO thorough reassignment tests
    
    
        #OVERLAPPING KEYS TESTING
        
        #class member
        ut.assertEqual(self.f, {"x":0.6})
        ut.assertEqual(self.f["x"], 0.6)
        # reassignment
        self.f["x"] = 0.7
        ut.assertEqual(self.f, {'x': 0.7})
        # deletion
        del self.f
        
        #second dict (highest priority that has the key)
        ut.assertEqual(self.f, {'y': 6})
        ut.assertEqual(self.f.y, 6)
        # reassignment
        self.f.y = 7
        ut.assertEqual(self.f, {'y': 7})
        ut.assertEqual(self.f.y, 7)
        # deletion
        del self.f
        
        #third dict (lowest priority)
        ut.assertEqual(self.f, {'z': 66})
        # reassignment
        self.f["z"] = 77
        ut.assertEqual(self.f, {'z': 77})
        #deletion
        del self.f
        
        #key is now fully gone
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
