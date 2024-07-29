from math import *
from turtle import *

# Assignment 1
#
# Author's Name: SIM SHANG EN
# Author's ID:
#

# Task 1: absolute difference between two roots
# =============================================

# Insert your comments about function rootAbsDiff() below


def rootAbsDiff(a, b, c):
    # Quadratic formula
    # x = (-b (+/-) sqrt(b^2-4ac)) / 2a
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    # Calculate the two roots
    root1 = (-b + sqrt(discriminant)) / (2 * a)
    root2 = (-b - sqrt(discriminant)) / (2 * a)

    # Calculate and return the absolute difference between the roots
    return abs(root1 - root2)


##print(rootAbsDiff(1, 2, 1))
##print(rootAbsDiff(1, 7, 10))
##print(rootAbsDiff(3, 8, 3.5))

# Task 2: polygon area
# ====================

# Insert your comments about function areaPoly() below


def areaPoly(n, d):
    # Calculate the perimeter
    perimeter = n * d

    # Calculate the apothem (convert degrees to radians for tan function)
    apothem = d / (2 * tan(pi / n))

    # Calculate and return the area
    return (perimeter * apothem) / 2


# Insert your comments about function polySide() below


def polySide(n, area):
    # We need to solve the equation: area = (n * d^2) / (4 * tan(pi/n))
    # Rearranging to isolate d:
    # d = sqrt((4 * area * tan(pi/n)) / n)

    d = ((4 * area * tan(pi / n)) / n) ** 0.5

    return d


##>>> areaPoly(4,10)
##100.00000000000001
##>>> polySide(4,100)
##10.0
##>>> areaPoly(4,polySide(4,100))
##100.00000000000001
##>>>

# Turtle graphic: draw a house
# ============================

# Insert your comment about function draw_house() below


def draw_house(height, breadth, roof_base):
    # draw a house of certain height, and certain breadth
    # and certain roof base, as governed by the respective
    # parameters.
    roof_overhang = (roof_base - breadth) / 2
    pd()
    fd(breadth)
    right(90)
    bk(height)
    left(90)
    fd(roof_overhang)
    left(120)
    fd(roof_base)
    left(120)
    fd(roof_base)
    left(120)
    fd(roof_overhang)
    left(90)
    bk(height)
    left(90)
    pu()


# draw_house(100, 150, 200)
