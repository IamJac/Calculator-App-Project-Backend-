from sympy import sympify
class Bodmas:
    def __init__(self,input_string):
        self.input_str=input_string

    def bodmas_calculator(self):
        try:
            result = sympify(self.input_str)
            return result
        except Exception as e:
            print(e)