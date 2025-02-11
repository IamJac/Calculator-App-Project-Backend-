from sympy import symbols,sympify,diff,integrate,lambdify
from scipy.differentiate import derivative
from scipy.integrate import quad

class Differentiation:
    def __init__(self,input_str):
        self.expression1=input_str

    def symbolic_derivative(self):
        x=symbols("x")
        expr1=sympify(self.expression1)
        symbolic_derivation=diff(expr1,x)
        return symbolic_derivation

    def numeric_derivative(self,x_value,n):
        x = symbols("x")
        expr1 = sympify(self.expression1)
        numerical_function = lambdify(x, expr1, 'numpy')
        numerical_derivative = derivative(numerical_function, x_value, order=n, step_factor=1e-6)
        return numerical_derivative


class Integration:
    def __init__(self,input_str):
        self.expression1=input_str

    def indefinite_integration(self):
        x=symbols("x")
        expr1=sympify(self.expression1)
        indefinite_integral=integrate(expr1,x)
        return indefinite_integral

    def definite_integral(self,upper_bound,lower_bound):
        x = symbols("x")
        expr1 = sympify(self.expression1)
        numerical_function = lambdify(x, expr1, 'numpy')
        definite_integral = quad(numerical_function, upper_bound, lower_bound)
        return definite_integral
