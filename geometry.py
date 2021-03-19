def nx(a, q, n):
    an = a * q ** (n-1)
    return an


def suma_n(a, q, n):
    if q == 1:
        suma = a * n
        return suma
    else:
        suma = a * ((1-q**n)/(1 - q))
        return suma
