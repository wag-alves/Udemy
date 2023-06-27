class Camera:
    def __init__(self, nome, filmando=False):
        self. nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'Já está filmando!')
            return
        
        print(f'Esta {self.nome} filmando...')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome}NÃO está filmando...')
            return
        
        print(f'{self.nome} esta parando de filmar...')
        self.filmando = False


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c2.filmar()