def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return  decimal_a_binario(num // 2) + str(num % 2)

print(decimal_a_binario(5))
