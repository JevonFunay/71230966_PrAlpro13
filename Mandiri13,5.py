def kombinasi(x, y):
    if x < y:
        return 0
    
    if y == 0 or y == x:
        return 1
    
    return kombinasi(x - 1, y - 1) + kombinasi(x - 1, y)


print(kombinasi(4, 2))
