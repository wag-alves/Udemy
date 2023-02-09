'''
num = int(input(f'Digite um número: '))

if num == float or num == str:  
    print(f'ERROR')

elif num % 2 == 0:
    if num > 0:
        print(f'O número é par positivo!')
    else:
        print(f'O número é par negativo!')

else:
    if num > 0:
        print(f'O número é ímpar positivo!')
    else:
        print(f'O número é ímpar negativo')
        
'''
'''
hora = float(input(f'Olá, que horas são? '))

if hora >= 0 and hora < 12:
    print(f'Então já é Bom dia! ')
elif hora >= 12 and hora < 18:
    print(f'Então já é Boa tarde! ')
else:
    if hora >= 18 and hora < 24:
        print(f'Tá tarde, já é hora de dormir! ')
    else:
        print(f'Horário inválido! ')

'''
'''
nome = str(input(f'Digite seu nome: '))
tamanho = len(nome)

if tamanho <= 4:
    print(f'Seu nome é curto! ')
elif tamanho <= 6:
    print(f'Seu nome é normal! ')
else:
    print(f'Seu nome é muito grande! ')


    '''
'''

nome = 'WAgner aLves DE Souza'

print(nome.upper()) #Tudo maiúsculo
print(nome.lower()) #Tudo minúsculo
print(nome.title()) #Primeiras letras maiúsculas

'''