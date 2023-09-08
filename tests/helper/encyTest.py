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

class encyTestSimple(ency):
    def __init__(self):
        self.dot1 = {"a": 1, "b": 2}
        super().__init__(("dot1"))