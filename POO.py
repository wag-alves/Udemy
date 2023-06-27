class Carro:
    def __init__(self, nome):
        self.nome = nome

    def marca(self):
        print(f'{self.nome}')

x = Carro('Ford ka')
Carro.marca(x) #não é usual...
x.marca()