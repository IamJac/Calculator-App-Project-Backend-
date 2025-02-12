from math import pow
class Roots:
    def __init__(self,x,n):
        self.number=x
        self.root=n
    def nth_root(self):
        return float(pow(self.number,1/self.root))
