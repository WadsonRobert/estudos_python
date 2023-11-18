def espaco():
    print('_'*30)

print('Descubra o ponto do seu cozimento')
espaco()

while True:
    
    print('Primeiro devemos saber se a temperatura está em Celsius ou Fanhreit')
    print('')
    print('Celsius: 1')
    print('Fahnreit: 2')
    print('Sair : 0')
    escolha = int(input('Digite a seguir: '))
    espaco()       
    
    if escolha == 1:
        c = int(input('Digite os Graus da carne em Celsius: '))
        print('')
        if 48 <= c <= 53:
            print('O ponto da sua carne é RARE (Selada).')
            espaco()
        elif 54 <= c <= 59:
            print('O ponto da sua carne é Medium RARE (Ao ponto para mal).')
            espaco()
        elif 60 <= c <= 64:
            print('O ponto da sua carne é MEDIUM (Ao ponto).')
            espaco()
        elif 65 <= c <= 70:
            print('O ponto da sua carne é Medium well (Ao ponto para o bem).')
            espaco()
        elif c >= 71:
            print('O ponto da sua carne é Well done (Bem passada).')
            espaco()
        elif 48 < c:
            print('Sua carne está crua.')
            espaco()


    elif escolha == 2:
        f = int(input('Digite os Graus da carne em Fahnreit: '))
        print('')
        if 120 <= f <= 129:
            print('O ponto da sua carne é RARE (Selada).')
            espaco()
        elif 130 <= f <= 139:
            print('O ponto da sua carne é Medium RARE (Ao ponto para mal).')
            espaco()
        elif 140 <= f <= 149:
            print('O ponto da sua carne é MEDIUM (Ao ponto).')
            espaco()
        elif 150 <= f <= 159:
            print('O ponto da sua carne é Medium well (Ao ponto para o bem).')
            espaco()
        elif f >= 160:
            print('O ponto da sua carne é Well done (Bem passada).')
            espaco()
        elif f < 120:
            print('Sua carne está crua.')
            espaco()
    if escolha == 0:
        print('Programa fechado com sucesso, Obrigado')
        break
