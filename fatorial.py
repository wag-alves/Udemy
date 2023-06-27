

def factorial(n):
    if n <= 1:
        return 1
    if n >= 1000:
        return f'Sou limitado, não sei calcular isso.'
    return n * factorial(n-1)


print(factorial(4))
print(factorial(5))
print(factorial(999))
print(factorial(0))
print(factorial(-20))
print(factorial(1000))
