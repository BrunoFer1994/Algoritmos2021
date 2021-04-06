#factorial iterativo
def factorial_1 (numero):
    factorial = 1
    for i in range(2,6):
        factorial = factorial * i
    return factorial

print (factorial_1(5))

#factorial recursivo
def factorial_2 (numero):
    if(numero == 1 or numero == 0):
        return 1
    else:
        return numero * factorial_2(numero - 1)

print (factorial_2(5))


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
    
print(fibonacci_i(7))

#Fibonacci Recursivo
def fibonacci_r (numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return fibonacci_r(numero-1) + fibonacci_r(numero-2)
print(fibonacci_r(8))