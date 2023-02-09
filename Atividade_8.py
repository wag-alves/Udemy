

x = 0 #É coluna
# y = 0 É linha

while x <= 5:
    y = 0 # o Y tem que zerar toda vez que entrar...
    while y <= 5:
        print(f'O valor de X é {x} e Y é {y}')
        y += 1
    x += 1
print('Fim.')