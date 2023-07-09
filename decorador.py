def decorator(func):
    def inner(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return inner

def reverse_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('parametro não é uma string')
    
checking = decorator(reverse_string)
reverse = checking('123')
print(reverse)


def decorator_two(func):
    def inner(*args, **kwargs):
        for arg in args:
            is_string_two(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return inner

@decorator_two
def reverse_string_two(string):
    return string[::-1]

def is_string_two(param):
    if not isinstance(param, str):
        raise TypeError('parametro não é uma string')
    
reverse2 = reverse_string_two('wagner')
print(reverse2)