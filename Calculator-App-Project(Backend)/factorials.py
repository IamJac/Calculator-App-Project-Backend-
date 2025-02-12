from math import factorial,perm,comb
class Factorial:
    def __init__(self,n):
        self.number=n
    def calculate_factorial(self):
        return factorial(self.number)

class Permutations:
    def __init__(self,n,k):
        self.given_terms=k
        self.terms=n
    def determine_permutations(self):
        return perm(self.given_terms,self.terms)
class Combinations:
    def __init__(self,n,k):
        self.given_terms=k
        self.terms=n
    def determine_combinations(self):
        return comb(self.given_terms,self.terms)