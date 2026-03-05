# Aritmética. Escreva um programa Python que leia do usuário dois inteiros a e b. Seu
# programa deve computar e exibir o seguinte:
# • A soma de a e b
# • A diferença quando b é subtraído de a
# • O produto de a por b
# • O quociente quando a é dividido por b
# • O resto quando a é dividido por b
# • O resultado de log10a
# • O resultado de a^b

import math #contas

print("ARITMÉTICA\n\n")
a = int(input("Insira seu número A: "))
b = int(input("Insira seu núemro B: "))

print("\nA soma " , a + b)
print("A diferença quando B é subtraído de A: ", a - b)
print("O produto de ambos: ", a * b)
print("O quociente de A por B: ", a/b)
print("O resto da divisão de A por B: ", a%b)
print("O resultado de log10 de A: ", math.log10(a)) #log
print("O resultado de A^B: ", a ** b)