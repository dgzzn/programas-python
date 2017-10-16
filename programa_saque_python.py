print('Valor mínimo: R$ 10')
print('Valor máximo: R$ 600')
valor = int(input('Digite o valor do saque: '))


def cemRedondo(valor):  # 100, 200, 500
    notas_cem = valor // 100
    print('{} notas de R$ 100'.format(notas_cem))

def notasDez(valor):
    notas_10 = valor // 10
    print('{} nota(s) de R$10'.format(notas_10))
    menorCinquenta(valor % 10)

def menorCinquenta(valor):  # recebe o resto do modulo por cem
    
    if 0 < valor % 10 < 5:  # se o resto for de 1 a 4, dá notas de 1 real
        notas_1 = valor % 10
        print('{} nota(s) de R$1'.format(notas_1))
    elif valor % 10 == 5:  # se for exatamente igual a 5, dá nota de 5
        notas_5 = valor % 10
        print('{} nota(s) de R$5'.format(notas_5))
    elif valor % 10 == 10:  # se for exatamente igual a 10, dá nota de 10
        notas_10 = valor % 10
        print('{} nota(s) de R$10'.format(notas_10))
    elif 5 < valor % 10 < 10:  # se for maior que 5 e menor que 10
        notas_1 = valor % 5
        notas_5 = int(5/(valor-notas_1))  # pega o valor e dá a nota de 5 e subtrai os 5 do valor
        print('{} nota(s) de R$5.'.format(notas_5))
        print('{} nota(s) de R#1'.format(notas_1))

def maiorCinquenta(valor):
    nota_50 = valor // 50
    print('{} nota de R$50.'.format(nota_50))
    maiorVinte(valor%50)
    #notasDez(valor%50)
    #menorCinquenta(valor%50)

def maiorVinte(valor):
    notas_20 = valor // 20
    print('{} notas de R$20.'.format(notas_20))
    notasDez(valor%20)

if (valor < 10) or (valor > 600):
    print('Valor inválido! ')

elif valor < 100:
    maiorVinte(valor)
    #notasDez(valor)
    #notas_10 = valor // 10
    #print('{} nota(s) de R$10'.format(notas_10))
    #menorCinquenta(valor % 10)

elif valor >= 100:
    resto = valor%100
    cemRedondo(valor)

    if resto < 50:
        maiorVinte(resto)
    else:
        maiorCinquenta(resto)
