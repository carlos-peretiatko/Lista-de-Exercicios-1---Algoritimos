# Juros compostos.
#  Faça de conta que você acabou de abrir uma conta de investimento que
# rende 12% de juros ao ano. Os juros que você ganha são pagos ao final do ano. Escreva um
# programa que começa lendo do usuário o valor inicial depositado na conta. Em seguida, o
# programa deve computar e exibir o saldo da conta de investimento após 1, 2 e 3 anos. Exiba
# cada valor com exatamente 2 casas decimais.

#0,12 = 12%
import time #delay
import os #clear
os.system('cls' if os.name == 'nt' else 'clear') #definição

print("BEM VINDO AO BANCO!\nAQUI SEU DINHEIRO RENDE EXATAMENTE 12% AO ANO!")
time.sleep(2)
os.system('cls')


deposito = float(input("Insira o valor do seu deposito inicial: "))

print("Com essa quantidade ao longo dos anos você terá: ")

for i in range(3): #prit mais inteligente
    deposito = (deposito*0.12)+deposito
    print("No ano ", i+1 , f":  R${deposito:.2f}!")
      
