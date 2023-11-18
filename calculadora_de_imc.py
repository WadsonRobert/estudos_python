print('Calculo de IMC - Indice de Massa Corporal')
print('')

#Variaveis altura e peso que coleta os dados do usuario
altura = float(input('Qual a sua altura em CM: '))
peso = float(input('Qual é o seu peso em KG: '))

altura_calc = altura / 100


#Variavel IMC que calcula o peso e altura, e entrega o resultado
imc = peso / (altura_calc * 2)

#loop com os indices de cada imc
while True:
    if imc < 18.5:
        print(f'Seu IMC é {imc:.2f}, e é considerado MAGREZA')
    elif 18.5 <= imc <= 24.9:
        print(f'Seu IMC é {imc:.2f}, e é considerado NORMAL')
    elif 25.0 <= imc <= 29.9:
        print(f'Seu IMC é {imc:.2f}, e é considerado SOBREPESO')
    elif 30.0 <= imc <= 39.9:
        print(f'Seu IMC é {imc:.2f}, e é considerado OBESIDADE')
    elif imc >= 40:
        print(f'Seu IMC é {imc:.2f}, e é considerado OBESIDADE GRAVE')
    print('')
    print('_'*30)
    
    #Variavel para dar stop no programa
    parar = int(input('Caso deseje SAIR digite "0", para CONTINUAR digite "1" '))
    if parar == 0:
        print('Programa fechado com sucesso, Obrigado')
        break




