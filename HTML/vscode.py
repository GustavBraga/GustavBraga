def decompor_valor(valor):
    notas = [200, 100, 50, 20, 10, 5, 2]

    quantidade_notas = {}

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
               quantidade_notas[nota] = quantidade
               valor -= quantidade * nota 

    return quantidade_notas


valor = int(input("Digite o valor para decompor: "))
quantidade_notas = decompor_valor(valor)

print(f"Decomposição do valor {valor}:")
for nota, quantidade in quantidade_notas.items():
    print(f"{quantidade} notas de {nota} reais")