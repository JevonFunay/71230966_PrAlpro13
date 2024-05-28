def bilanganprima(a, pembagi = 2):
    if a < 2:
        return False
    if pembagi > int(a**0.5):
        return True
    if a % pembagi == 0:
        return False
    return bilanganprima(a, pembagi + 1)

print(bilanganprima(11))