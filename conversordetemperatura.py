print('Olá, Seja bem-vindo ao nosso programa que converte as temperaturas')
print('')
print('_' *40)
print('Primeiro você deve escolher qual a conversão que deseja fazer')
print('caso seja de Celsius para Fahrenheit digite : 1')
print('ou se for de Fahrenheit para Celsius digite : 2')
print('para fechar o programa digite: 0')
print('_' *40)

while True:
 #aqui o usuario vai digite qual o número da conversão que deseja
 escolha = int(input('Digite 1 ou 2, ou para fechar o programa "0" : '))
 print('_' *40)
 
 if escolha == 1:
        temp = input(print('Agora nós diga qual a temperatura que você deseja que seja convertida, apenas o numero: '))
        temperatura = float(temp)
        conversaoCF = (temperatura * 9/5)+32
        print(f'A conversão da temperatura escolhida de {temperatura} graus Celsius em Fahrenheit é igual a = {conversaoCF} Graus')
        print('_' *40)
 elif escolha == 2:
        temp = input(print('Agora nós diga qual a temperatura que você deseja que seja convertida, apenas o numero: '))
        temperatura = float(temp)
        conversaoFC = (temperatura - 32) * 5/9
        print(f'A conversão da temperatura escolhida de {temperatura} graus Fahrenheit em Celsius é igual a = {conversaoFC} Graus')
        print('_' *40)
 elif escolha == 0:
       print('Programa fechado, Obrigado por usar!')
       break
 else:
        print('Você não digitou um número correto, tente novamente')
        print('')
        print('_' *40)
        