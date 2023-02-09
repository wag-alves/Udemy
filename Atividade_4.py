
num1 = input(f'Digite um número: ')
num2 = input(f'Digite um número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')