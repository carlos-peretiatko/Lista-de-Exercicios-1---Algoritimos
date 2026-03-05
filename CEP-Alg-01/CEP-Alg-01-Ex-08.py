# Bugigangas e quinquilharias. 
# Uma loja online oferece aos seus clientes dois tipos de
# produto: bugigangas e quinquilharias. Cada bugiganga pesa 75 gramas e cada quinquilharia
# pesa 112 gramas. Faça um programa Python que leia a quantidade de bugigangas e a
# quantidade de quinquilharias de um pedido do usuário. A seguir, seu programa deve calcular e
# exibir o peso total do pedido.

#1 kilo = 1000 gramas 
#75 = 0,0075
#112 = 0,112

import os #limpa tela
os.system('cls' if os.name == 'nt' else 'clear') #definicao de nome
import time #delay

key = -1 #chave para finalizar pedido 

bugiganga = 0 #acumulador 
quinquilharia = 0 #acumulador


print("BEM VINDO A BUGIGANGAS E QUINQUILHARIAS!!")

for i in range(3): #apenas estetica de espera 
    print('.')
    time.sleep(1)

while key != 0:
    #reciclagem do exe5

    os.system('cls') #limpa tela comando 
    print("Bugiganga     (1 litro ou menos) - 1")
    print("Quinquilharia   (mais de um litro) - 2")
    print("Sair - 0")
    print("\nPeso total do pedido:" , (bugiganga*0.0075) + (quinquilharia*0.112))
    key = int(input("\nInforme o tamanho da embalagem que deseja adicionar: "))
    
    match key: #swich
        case 1:
            bugiganga += 1
        case 2: 
            quinquilharia += 1
        case 0:
            break
        case _: 
            print("Opção inválida, por favor retorne e selecione uma opção sugerida")

print("\nPrograma finalizado com sucesso!")
print("Seu pedido teve o peso de: ", (bugiganga*0.0075) + (quinquilharia*0.112), "kg")
    