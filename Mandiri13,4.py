def hitungbilangan (n):
    if n == "":
        return 0
    if n[0].isdigit():
        return int(n[0]) + hitungbilangan(n[1:])
    else:
        return hitungbilangan(n[1:])
    
print(hitungbilangan("123"))

    