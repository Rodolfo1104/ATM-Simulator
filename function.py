def calcular_notas_para_saque(valor_saque):
    notas_disponiveis = [100, 50, 10, 5, 1]
    notas_fornecidas = {}

    for nota in notas_disponiveis:
        quantidade_notas = valor_saque // nota
        if quantidade_notas > 0:
            notas_fornecidas[nota] = quantidade_notas
            valor_saque -= quantidade_notas * nota

    return notas_fornecidas