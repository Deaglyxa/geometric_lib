import math


def area(r):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r


def perimeter(r):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * r
