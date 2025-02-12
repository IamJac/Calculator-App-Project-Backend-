from math import gcd,lcm
from functools import reduce
class Factors:
    def __init__(self,integers1):
        self.integers=integers1
    def greatest_common_divisor(self):
        return reduce(gcd,self.integers)
    def least_common_factor(self):
        return reduce(lcm, self.integers)