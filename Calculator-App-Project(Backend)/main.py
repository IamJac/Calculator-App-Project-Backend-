from time import sleep
from math import inf
import subprocess
from bodmas import Bodmas
from calculus import Differentiation,Integration
# import os
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("                                                                  CALCULATOR APP")
sleep(3)
subprocess.run('cls', shell=True)
# os.system("cls" if os.name=="nt" else "clear")
choice = 0
choice2 = 0
choice3 = 0
while choice < inf:
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("                                                    CHOOSE YOUR PREFERRED OPERATION BELOW (ie 1,2,3... etc)")
    print(" ")
    print("                                                       [Input 10 to quit]")
    print(" ")
    print("                                                    1 - BODMAS OPERATIONS ie (),+,* etc")
    print("                                                    2 - CALCULUS")
    print("                                                    3 - PERMUTATIONS,COMBINATIONS AND FACTORIALS")
    print("                                                    4 - GCD AND LCM")
    print("                                                    5 - Nth ROOTS ie square root")
    print("                                                    6 - LOGARITHMS")
    print("                                                    7 - TRIGONOMETRY")
    print("                                                    8 - BINARY,HEXADECIMAL,OCTAL AND DECIMAL NUMBER SYSTEMS")

    try:
        choice = int(input("Your option \n"))
    except Exception as e:
        print("Wrong input type(input should be an option among the specified ones)")
        continue

    if choice == 1:
        print("Input your expression to be computed")
        expression = str(input("input \n"))
        obj1 = Bodmas(expression)
        result1 = obj1.bodmas_calculator()
        print(F"Answer = {result1}")
        subprocess.run('cls', shell=True)
        # os.system("cls" if os.name=="nt" else "clear")
        continue
    elif choice == 2:
        while choice3>(-inf):
            print("                                                   CHOOSE")
            print("                                                   1 - Definite Integration")
            print("                                                   2 - Indefinite Integration")
            print("                                                   3 - Symbolic Differentiation")
            print("                                                   4 - Derivative at a point")

            choice3=int(input("Input \n"))
            if choice3==1:
                try:
                    expression1 = str(input("input \n"))
                except Exception as e:
                    continue
                obj2 = Integration(expression1)
                l = int(input("Lower bound \n"))
                u = int(input("Upper bound"))
                result2 = obj2.definite_integral(u, l)
                print(F"Answer = {result2}")
                subprocess.run('cls', shell=True)
                # os.system("cls" if os.name=="nt" else "clear")
                continue

            elif choice3==2:
                try:
                    expression2 = str(input("input \n"))
                except Exception as e:
                    continue
                obj3 = Integration(expression2)
                result3 = obj3.indefinite_integration()
                print(F"Answer = {result3}")
                subprocess.run('cls', shell=True)
                # os.system("cls" if os.name=="nt" else "clear")
                continue

            elif choice3==3:
                try:
                    expression3 = str(input("input \n"))
                except Exception as e:
                    continue
                obj4 = Differentiation(expression3)
                result3 = obj4.symbolic_derivative()
                print(F"Answer = {result3}")
                subprocess.run('cls', shell=True)
                # os.system("cls" if os.name=="nt" else "clear")
                continue
            elif choice3==4:
                try:
                    expression5 = str(input("input \n"))
                except Exception as e:
                    continue
                obj5 = Differentiation(expression5)
                point = float(input("x_value-a point to evaluate the rate of change \n"))
                order = int(input("order of the derivative ie nth order derivative \n"))
                result1 = obj5.numeric_derivative(point, order)
                print(F"Answer = {result1}")
                subprocess.run('cls', shell=True)
                # os.system("cls" if os.name=="nt" else "clear")
                continue
            else:
                print("Invalid input")
                continue
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 10:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("                                                            Sure you want to quit")
        print("                                                                  1- YES")
        print("                                                                  2- NO")
        try:
            choice2 = int(input("Your choice \n"))
        except Exception as e:
            print("Invalid input type")
            continue
        if choice2 == 1:
            subprocess.run("cls", shell=True)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("                                                           QUITTING")
            break
        else:
            subprocess.run("cls", shell=True)
            continue
    else:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")

        print("                                                           INVALID INPUT")
        continue
    choice += 1





