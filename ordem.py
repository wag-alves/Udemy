
pessoas = [
    {'nome' : 'Wagner' , 'sobrenome' : 'Alves'},
    {'nome' : 'Larissa' , 'sobrenome' : 'Deborah'},
    {'nome' : 'Désirée' , 'sobrenome' : 'Noronha'},
    {'nome' : 'José' , 'sobrenome': 'Alves'}
]

def ordem (item):
    return item['nome']

pessoas.sort(key=ordem)

#pessoas.sort(key=lambda item: item['nome'])

for pessoa in pessoas:
    print(pessoa)
