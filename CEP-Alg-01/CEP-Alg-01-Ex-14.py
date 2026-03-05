# Área de um triângulo (novamente). No exercício anterior você criou um programa para
# calcular a área de um triângulo dados sua base e sua altura. Entretanto, também é possível
# calcular a área de um triângulo se forem conhecidos os comprimentos de seus 3 lados. Seja
# l1, l2, e l3 os comprimentos dos três lados.

#L = (l1 + l2 + l3)/2

# Então, a área do triângulo pode ser calculada com a seguinte fórmula:

#a = raiz de L * (L - l1) * (L - l2) * (L - l3)

# Escreva um programa Python que leia os comprimentos de 3 lados de um triângulo, calcule e
# exiba sua área.

import math #raiz = math.sqrt(16)

print("ÁREA DO TRIÂNGULO 2!!\n\n")

l1 = float(input("Informe o valor do primeiro lado do seu triângulo: "))
l2 = float(input("Informe o valor do segundo lado do seu triângulo: "))
l3 = float(input("Informe o valor do terceiro lado do seu triângulo: "))

L = (l1 + l2 + l3)/2 #formula comprimento

a = math.sqrt(L * (L - l1) * (L - l2) * (L - l3)) #formula área # desnecessario guardar essa variavel 

print(f"A área do triângulo informado é:  {a:.2}" , "\nPitágoras esta muito orgulhoso :)")