# Retorno de recicláveis. Alguns estabelecimentos retornam créditos em troca de reciclagem
# de recipientes. Em um estabelecimento em particular, vasilhames de um litro ou menos geram
# crédito de 10 centavos e vasilhames de mais de um litro geram créditos de 25 centavos.
# Escreva um programa que leia do teclado a quantidade destes dois tipos de vasilhames a
# serem reciclados. A seguir o programa deve calcular e exibir o valor total dos créditos
# referentes ao retorno dos vasilhames. Pesquise sobre como formatar a saída para que a
# resposta seja exibida com sinal de reais R$ e exatamente duas casas decimais.

key = -1 #chave basica
litroPequeno = 0 #acumulador
litroGrande = 0 #acumulador

while key != 0:
    total = (litroPequeno*0.1)+(litroGrande*0.25) #0,25 == 25% 
    
    print(f"saldo atual: R${total:.2f}")
    print("Litro pequeno (1 litro ou menos) - 1")
    print("Vasilhame grande (mais de um litro) - 2")
    print("Sair - 0")
    key = int(input("\nInforme o tamanho da embalagem que deseja adicionar: "))
    
    match key: #swich
        case 1:
            litroPequeno += 1
        case 2: 
            litroGrande += 1
        case 0:
            break
        case _: 
            print("Opção inválida, por favor retorne e selecione uma opção sugerida")
        
print("Programa finalizado com sucesso!!")
print(f"saldo total: R${total:.2f}")