class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print('Removendo a instância da classe.')
    
    
    def falar(self):
        print('AuAu')
    
def criar_cachorro(self):
    c = Cachorro('Zeus', 'Branco e preto', False)
    print(c.nome)


c = Cachorro('Chappie', 'amarelo')
c.falar()

print('Ola mundo')

del c

print('Ola mundo')
print('Ola mundo')
print('Ola mundo')


# criar_cachorro()

