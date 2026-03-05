# Área de uma sala. Escreva um programa Python que peça para o usuário os comprimentos
# da largura e profundidade de uma sala. Após a leitura dos valores, seu programa deve exibir a
# área da sala. A largura e a profundidade devem ser números reais. Inclua as unidades nas
# mensagens de entrada e saída (metros e metros quadrados). 

comp = float(input("Informe o comprimento da largura da sua sala: "))
prof = float(input("Informe a profundidade da sua sala: "))

area = comp * prof

print("Sua sala possui \nlargura: " , comp , "m\nprofundidade: " , prof , "m\narea: " , area , "m²")