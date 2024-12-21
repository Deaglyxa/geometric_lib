import circle
import square

figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {
    "circle-area": 1,
    "circle-perimeter": 1,
    "square-area": 1,
    "square-perimeter": 1,
}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input(
                    "Input figure sizes separated by space, 1 for circle and square\n"
                ).split(" "),
            )
        )

    result = calc(fig, func, size)
    print(f"{func} of {fig} is {result}")
