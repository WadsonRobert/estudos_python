funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#lista de funcionarios que contem cada especificação
lista_carro_noite = []
lista_carro_dia = []
lista_sem_carro =  []

#Verifica quem está em turno noite, e se a pessoa tem carro
for pessoas1 in turno_noite:
    if pessoas1 in tem_carro:
        lista_carro_noite.append(pessoas1)

#Verifica quem está em turno dia, e se a pessoa tem carro
for pessoas2 in turno_dia:
    if pessoas2 in tem_carro:
        lista_carro_dia.append(pessoas2)

#Verifica quem não tem carro
for pessoas3 in funcionarios:
    if pessoas3 not in tem_carro:
        lista_sem_carro.append(pessoas3)



print(f' Essa é a lista de funionarios que trabalham a noite e possuem carro, {lista_carro_noite}')
print(f' Essa é a lista de funionarios que trabalham de dia e possuem carro, {lista_carro_dia}')
print(f' Essa é a lista de funionarios não possuem carro, {lista_sem_carro}')