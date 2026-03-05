# Soma dos n primeiros números positivos. Escreva um programa Python que receba do
# usuário um número inteiro positivo n e então exiba a soma de todos os números inteiros de 1 a
# n. Tal soma pode ser computada usando a seguinte fórmula:
#(n)(n+1)/2

n = int(input("Insira um numero inteiro positivo: "))

if n < 0:
    print("Isso é um número negativo!")
else:
    print((n)*(n+1)/2) #calculo 