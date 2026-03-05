# Área de um triângulo. A área de um triângulo pode ser calculada pela fórmula abaixo, onde b
# é o comprimento de sua base e h é o comprimento de sua altura.

# Escreva um programa Python que permita que o usuário forneça os dados de b e h de um
# triângulo, e calcule e exiba o valor de sua área.

# a = (b * h) / 2

print("Área do triângulo")

b = float(input("Informe o valor da base do triâgulo: "))
h = float(input("Informe a altura do triângulo: "))

a = (b * h) / 2

print(f"A área do triangulo informado é:  {a:.2} ", "\nPitágoras estaria orgulhoso :)")