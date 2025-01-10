def Multiples(dado):
    i=0
    sum = 0
    while i<=dado:
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
        i += 1
    return sum


