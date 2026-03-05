# Área e volume. Escreva um programa Python que começa lendo o valor de um raio r,
# fornecido pelo usuário. O programa deve continuar calculando e exibindo a área de um círculo
# de raio r, e o volume de uma esfera de raio r. Utilize a constante pi do módulo math nos seus
# cálculos.

# a = pi*r²     ---    v = 4/2*pi*r³

import math

print("ÁREA E VOLUME\n\n")

r = float(input("Informe o raio do seu círculo: "))

#operações 
a = math.pi * r ** 2
v = (4/2) * math.pi * r ** 3

print("A área do circulo com esse raio: " , a)
print("O volume da esfera com esse raio: " , v)