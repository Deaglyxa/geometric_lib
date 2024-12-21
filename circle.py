import math


def area(radius):
    if radius <= 0:
        raise ValueError("Side lengths must be positive.")
    return math.pi * radius * radius


def perimeter(radius):
    if radius <= 0:
        raise ValueError("radius lengths must be positive.")
    return 2 * math.pi * radius
