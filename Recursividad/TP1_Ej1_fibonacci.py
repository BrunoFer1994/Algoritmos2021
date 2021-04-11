#Fibonacci iterativo
def fibonacci_i (numero):
    fib_1 = 0
    fib_2 = 1
    fibonacci = 0
    for i in range(2, numero+1):
        fibonacci = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fibonacci
    return fibonacci
    
print(fibonacci_i(6))


#Fibonacci Recursivo
def fibonacci_r (numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return fibonacci_r(numero-1) + fibonacci_r(numero-2)

print(fibonacci_r(8))