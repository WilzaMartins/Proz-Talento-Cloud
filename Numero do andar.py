# Código para imprimir o número de cada andar de um hotel, excluindo o 13º andar.

# Definição das variáveis

total_andares = int(input("Qual o número total de andares do hotel?\n"))
nao_mostrar_andar = int(input("\nQual o número do andar que não deve ser exibido? \n\n"))

# Código utilizando for:

print("\n Resultado do código utilizando for:\n")

for i in range(1, total_andares + 1, 1):  # o incremento será iniciado em 1, irá até o número de andares do prédio+1 e será de 1 em 1

    if (i == nao_mostrar_andar):
        continue
    print(f"{i}º andar")

# Código utilizando while:

print("\n Resultado do código utilizando while:\n")

i = 0  # Valor inicial do contador
while (i < total_andares):
    i = i + 1
    if i == nao_mostrar_andar:
        continue
    print(f"{i}º andar")

# Código impressão em ordem decrescente :

print("\n Resultado do código impressão em ordem decrescente:\n")

for i in range(total_andares, 0, -1):  # o decremento será iniciado número de andares do prédio, até o número 0  e será de 1 em 1

    if (i == nao_mostrar_andar):
        continue
    print(f"{i}º andar")