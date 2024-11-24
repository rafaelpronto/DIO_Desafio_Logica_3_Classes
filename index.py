
class Hero():
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def ataque(self):
        match self.tipo:
            case 'MAGO': atk = 'MAGIA'
            case 'GUERREIRO': atk = 'ESPADA'
            case 'MONGE': atk = 'ARTES MARCIAIS'
            case other: atk = 'SHURIKEN'
        print(f'{self.tipo} {self.nome}, tem {int(self.idade) * 100} anos de idade.')
        print()
        print(f'{self.tipo} atacou usando {atk}.')    

def menuTipo():
    print()
    print('1 - Mago')
    print('2 - Guerreiro')
    print('3 - Monge')
    print('4 - Ninja')
    print()

nome = input('Digite o nome do Herói: ')
idade = input('Digite a idade do Herói: ')
menuTipo()
classe = int(input('Escolha o tipo: '))
match classe:
    case 1: tipo = 'MAGO'
    case 2: tipo = 'GUERREIRO'
    case 3: tipo = 'MONGE'
    case other: tipo = 'NINJA'

heroi = Hero(nome, idade, tipo)

print()

heroi.ataque()

print()
print('Até a próxima batalha!')
print()























