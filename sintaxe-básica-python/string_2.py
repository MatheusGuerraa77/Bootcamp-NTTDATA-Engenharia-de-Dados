nome = 'Matheus'
idade = 19
profissao = 'Programador'
linguagem = 'Python'

dados = {'nome': 'Matheus', 'idade': 19}

print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {nome} Idade: {idade}'.format(nome = nome, idade = idade))
print('Nome: {name} Idade: {age}'.format(age = 28, name=nome))
print('Nome: {name} Idade: {age} {name} {name} {age}'.format(age = idade, name=nome))
print('Nome: {nome} Idade: {idade}'.format(**dados))
print(f'Nome: {nome} idade: {idade}')