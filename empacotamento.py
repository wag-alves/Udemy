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