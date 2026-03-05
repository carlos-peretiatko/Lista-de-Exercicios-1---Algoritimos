# Área de um polígono regular. Um polígono é regular se seus lados são todos do mesmo
# tamanho e os ângulos entre lados adjacentes são todos iguais. A área de um polígono regular
# pode ser calculada pela fórmula abaixo onde l é o comprimento de um lado e n é o número de
# lados:

# a = (n * l ** 2) / (4 * math.tan(math.pi/n))

# Escreva um programa Python que obtenha do usuário os valores de l e n, e então calcule e
# exiba a área do polígono regular correspondente.

import math 

print("Área de um polígono regular!\n\n")

l = float(input("Informe o comprimento de um lado: "))
n = float(input("Agora informe o número de lados: "))

a = (n * l ** 2) / (4 * math.tan(math.pi/n)) #nao existe necessidade de armazenar

print(f"\nA área do polígono informado é: {a:.2} "  , "\nPitágoras esta definitivamente orgulhoso :)")

