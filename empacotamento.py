#para extrair informações de um dicionário eu uso **

pessoa = {
    'nome':'Wagner',
    'sobrenome': 'Alves'
}

dados = {
    'idade': 26,
    'altura': 1.94
}

dicio_completo = {**pessoa, **dados}
print(dicio_completo)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(f'Não nomeados: {args}')
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='José', qualquer_coisa=123)