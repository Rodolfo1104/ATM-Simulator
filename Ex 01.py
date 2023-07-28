def calcular_notas_para_saque(valor_saque):
    notas_disponiveis = [100, 50, 10, 5, 1]
    notas_fornecidas = {}

    for nota in notas_disponiveis:
        quantidade_notas = valor_saque // nota
        if quantidade_notas > 0:
            notas_fornecidas[nota] = quantidade_notas
            valor_saque -= quantidade_notas * nota

    return notas_fornecidas


def main():
    valor_minimo = 10
    valor_maximo = 600

    while True:
        valor_saque = int(input(f"Digite o valor do saque (entre {valor_minimo} e {valor_maximo} reais): "))

        if valor_minimo <= valor_saque <= valor_maximo:
            break
        else:
            print("Valor inválido! O valor do saque deve estar entre 10 e 600 reais.")

    notas_fornecidas = calcular_notas_para_saque(valor_saque)

    print("Notas fornecidas:")
    for nota, quantidade in notas_fornecidas.items():
        print(f"{quantidade} nota(s) de {nota} reais")

main()
