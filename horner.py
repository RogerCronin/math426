from functools import reduce

c = [5, -3, 2, 3, 4]

def horner(c: list[float], x: float) -> float:
    return reduce(lambda running_sum, ci: running_sum * x + ci, c)

print(horner(c, 2))
