def calculate_square_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side**2


def calculate_square_perimeter(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return 4 * side
