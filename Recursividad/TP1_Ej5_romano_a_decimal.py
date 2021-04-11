def romano_a_decimal(nromano):
    romanos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    Decimal = 0

    for i in range (len(nromano)):
        if i > 0 and romanos[nromano[i]] > romanos[nromano[i - 1]]:
            Decimal += romanos[nromano[i]] - 2 * romanos[nromano[i - 1]]
        else:
            Decimal += romanos[nromano[i]]
    return Decimal

print(romano_a_decimal('CXXI'))