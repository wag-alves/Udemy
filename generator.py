import sys

iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable)          # tem __iter__ e __next__

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

# aqui é guardado a lista completa, posso pegar qualquer indice
print(sys.getsizeof(lista))
# aqui eu sei a posição somente do primeiro elemento, por isso ocupa menos espaço na memória
print(sys.getsizeof(generator))


def generator(n=0):
    yield 1    # Pausa a Função
    print("Continuando...")
    yield 2    # Pausa a Função
    print("Mais uma vez...")
    yield from generator2()
    print("Fim.")
    return "ACABOU"


def generator2():
    yield 4
    print("olhai...")


gen = generator()
# print(gen.__next__())    esse é o modo "manual" de fazer
# print(next(gen))
# print(gen.__next__())
# print(next(gen))  #Aqui ele levanta uma exceção de StopIteration por causa do return


for item in gen:
    print(item)
