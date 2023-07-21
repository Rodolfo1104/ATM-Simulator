def calcular_notas(saque):
    notas_disponiveis = [100, 50, 10, 5, 1]
    notas_fornecidas = {}

    for nota in notas_disponiveis:
        notas_fornecidas[nota] = saque // nota
        saque %= nota

    return notas_fornecidas

def caixa_eletronico():
    valor_minimo = 10
    valor_maximo = 600

    while True:
        saque = int(input("Digite o valor do saque (entre {} e {} reais): ".format(valor_minimo, valor_maximo)))

        if valor_minimo <= saque <= valor_maximo:
            notas_fornecidas = calcular_notas(saque)
            print("\nNotas fornecidas:")
            for nota, quantidade in notas_fornecidas.items():
                if quantidade > 0:
                    print("{} nota(s) de {} reais".format(quantidade, nota))
            break
        else:
            print("Valor inválido. O valor do saque deve estar entre {} e {} reais.".format(valor_minimo, valor_maximo))
