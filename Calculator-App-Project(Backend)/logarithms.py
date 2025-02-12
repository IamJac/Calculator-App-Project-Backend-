from math import log
class Logarithms:
    def  __init__(self,b,m):
        self.base=b
        self.mantissa=m

    def calculate_logarithm(self):
        return float(log(self.mantissa,self.base))