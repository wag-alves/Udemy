
nome = str(input(f'Digite o seu nome: '))
senha = int(input(f'Digite a sua senha: '))

nome_bd = 'wagner'
senha_bd = 123456

if nome_bd == nome and senha_bd == senha:
    print(f'Sua senha provavelmente está correta...')

else:
    print(f'Vá simbora carniça')