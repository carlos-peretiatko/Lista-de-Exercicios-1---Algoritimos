# Área de um terreno. Crie um programa Python que leia as dimensões de um terreno em
# metros (largura e profundidade), e exiba o resultado em hectares.

larg = float(input("Insira a largura do seu terreno: "))
prof = float(input("Insira a profundidade do seu terreno: "))

#nao precisa armazenar a variavel
print("Seu terreno possui:\n" , larg , "m² de largura\n", prof , "m² de profundidade\n", (larg*prof)/10000 , " hectares")
