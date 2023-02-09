perguntas = [
    {
    'pergunta' : 'Quanto é 3X5? ',
    'option' : [20,15,10,25],
    'resposta' : 15
    },
    {
    'pergunta' : 'Quanto é 3X7? ',
    'option' : [20,15,21,25],
    'resposta' : 21
    },
    {
    'pergunta' : 'Quanto é 5X5? ',
    'option' : [20,15,10,25],
    'resposta' : 25
    }
]
cont = 0
r = 0
for item in perguntas:
    print(item['pergunta'])
    print()
    print(item['option'])
    print()
    x = int(input(f'Informe o valor da sua resposta: '))
    if x == item['resposta']:
        cont += 1
    else:
        r += 1
print(f'Você acertou {cont} vezes!! e errou{r}')








'''
print(perguntas[0]['pergunta'])
print(perguntas[0]['option'])
a = int(input(f'Qual a resposta? '))
if a == perguntas[0]['resposta']:
    print(f'Parabéns, você acertou! ')
else:
    print(f'Mais sorte na próxima ;) ')

print(perguntas[1]['pergunta'])
print(perguntas[1]['option'])
b = int(input(f'Qual a resposta? '))
if b == 21:
    print(f'Parabéns, você acertou! ')
else:
    print(f'Mais sorte na próxima! ') 

print(perguntas[2]['pergunta'])
print(perguntas[2]['option'])
c = int(input(f'Qual a resposta? '))
if c == 25:
    print(f'Parabéns, você acertou! ')
else:
    print(f'Mais sorte na próxima! ') 


'''