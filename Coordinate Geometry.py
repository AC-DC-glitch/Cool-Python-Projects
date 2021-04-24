import math
from math import*

A1 = input("INPUT THE 1ST X COORDINATE: ")
B1 = input("INPUT THE 1ST Y COORDINATE: ")
A2 = input("INPUT THE 2ND X COORDINATE: ")
B2 = input("INPUT THE 2ND Y COORDINATE: ")

Coordinate_1 = (float(A1), float(B1))
Coordinate_2 = (float(A2), float(B2))


a1_float = float(A1)
b1_float = float(B1)
a2_float = float(A2)
b2_float = float(B2)

Formula = input("Enter:\n1 for distance formula \n2 for midpoint formula:")

if Formula == "1":
    distance = str(math.sqrt(math.pow(a1_float-a2_float, 2) + math.pow(b1_float-b2_float, 2)))
    print("The distance between", Coordinate_1, "and", Coordinate_2,"is", distance)

if Formula == "2":
    midpoint = [((a1_float + a2_float)/2), ((b1_float + b2_float)/2)]
    print("The midpoint of", Coordinate_1, "and", Coordinate_2, "is", midpoint)