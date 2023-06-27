def soma_string(elem):
    variavel_final = elem
    def segunda(letra):
        nonlocal variavel_final
        variavel_final += letra
        return variavel_final
    return segunda

a = soma_string('a')
print(a('b'))
print(a('c'))
print(a('d'))
