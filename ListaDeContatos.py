#Lista de contatos

contatos = {}
contato2 = {}
print('_'*30)
print('')
print("Bem vindo ao gerenciador de contatos")
print('')
print('_'*30)

#Def com prints de tabela de funções
def menu():
  print('Digite 1 para cadastrar um contato')
  print('Digite 2 para buscar um contato')
  print('Digite 3 para EXCLUIR um contato')
  print('Digite 4 para ver todos os contatos da lista')
  print('Digite 0 para SAIR do programa')
  return

#Função para cadastrar os contatos
def cadastrar():
  if opcoes == 1:
    print('Digite o nome do contato que deseja salvar : ')
  nome = input('-')
  print('Digite o número do contato que deseja salvar : ')
  numero = input('-')
  contatos[nome] = numero
  return

#Função para buscar contatos adicionados
def buscar():
  if opcoes == 2:
    print('Digite o nome do contato que deseja buscar : ')
  nome = input('-')
  if nome in contatos:
    print('O número do contato é : ', contatos[nome])
  else:
    print('Contato não encontrado')
  return

#Função para excluir contatos adicionados
def exluir():
  if opcoes == 3:
    print('Digite o nome do contato que deseja exluir')
  nome = input('-')
  if nome in contatos:
    del contatos[nome]
  print('Contato excluido')
  return

#Função para sair do programa
def sair():
  if opcoes == 0:
    print('Programa fechado com sucesso')
  return

#Função para ver todos os contatos
def geral():
  if opcoes == 4:
    print(contatos)
  return
        
#Função para dar espaço
def espaco():
  print('_'*30)
  print('')

#Loop do programa
while True:
  menu()
  print('_'*30)
  print('')
  opcoes = int(input('Digite a opção desejada: '))
  if opcoes == 1:
    cadastrar()
    espaco()
  elif opcoes == 2:
    buscar()
    espaco()
  elif opcoes == 3:
    exluir()
    espaco()
  elif opcoes == 0:
    sair()
    espaco()
    break
  elif opcoes == 4:
    geral()
    espaco()
  else:
    print('Opção inválida')