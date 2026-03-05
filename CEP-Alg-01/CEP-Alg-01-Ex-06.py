# Conta do almoço. Imagine que você foi almoçar num restaurante, e pediu uma refeição com
# um suco, um prato principal e uma sobremesa. Cada um desses itens tem um preço unitário.

# Ao final, o valor da conta deve ser a soma do valor dos itens consumidos, acrescida de 10%
# de taxa de serviço. Faça um programa Python para receber estes dados do usuário e calcular
# o valor total da conta deste tipo de refeição. Exiba a resposta com os mesmos critérios de
# formatação da questão anterior (R$ e 2 casas decimais).

key = -1 #chave
total = 0.0
item = 0.0

while key != 0:
    item = float(input("Informe o valor do item consumido: "))
    total += item
    
    continua = input("Você possui mais itens ? (S/N)").upper()
    if continua == "S":
        key = -1
    else :
        key = 0
        
print(f"Total gasto no almoço : R${total:.2f}")