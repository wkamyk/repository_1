n = 3
def generuj(n):
    if n == 0:
        return"x"
    return "d" + generuj(n - 1)