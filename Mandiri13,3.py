def jumlahderetganjil(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + jumlahderetganjil(n - 1)


print(jumlahderetganjil(5))