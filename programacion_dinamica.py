import sys # para cambiar el recursion limit

# Fibonacci no eficiente
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1 

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fiblonacci con memoization
def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    # ver si n esta dentro del diccionario
    try:
        return memo[n]
    # si n no esta en el diccionario
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        # guardar resultado dentro del diccionario
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    sys.setrecursionlimit(20002)
    n = int(input('Escoge un numero: '))
    # resultado = fibonacci_recursivo(n)
    resultado = fibonacci_dinamico(n)
    print(resultado)