def area(side):
    if side <= 0:
        raise ValueError("Side lengths must be positive.")
    return side * side


def perimeter(side):
    if side <= 0:
        raise ValueError("Side lengths must be positive.")
    return 4 * side
