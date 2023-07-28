from function import calcular_notas_para_saque

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


