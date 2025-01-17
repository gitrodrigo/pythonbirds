class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joaquim = Pessoa(nome='Joaquim')
    vicente = Pessoa(nome='Vicente')
    rodrigo = Pessoa(joaquim,vicente, nome='Rodrigo')
    print(Pessoa.cumprimentar(rodrigo))
    print(id(rodrigo))
    print(rodrigo.cumprimentar())
    print(rodrigo.nome)
    print(rodrigo.idade)
    for filho in rodrigo.filhos:
        print(f'{filho.nome} é filho de {rodrigo.nome}')
    rodrigo.sobrenome = 'Pimentel'
    del rodrigo.filhos
    rodrigo.olhos = 1
    del rodrigo.olhos
    print(rodrigo.__dict__)
    print(joaquim.__dict__)
    print(vicente.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(rodrigo.olhos)
    print(vicente.olhos)
    print(id(Pessoa.olhos),id(joaquim.olhos), id(rodrigo.olhos))

