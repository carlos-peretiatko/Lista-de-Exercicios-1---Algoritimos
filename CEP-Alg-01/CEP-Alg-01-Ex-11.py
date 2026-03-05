# Distância entre dois pontos na terra. A terra é curva (a não ser para os terraplanistas! 😱 ) e
# a distância entre graus de longitude (leste-oeste) varia conforme a latitude (norte-sul). Com
# isso, encontrar a distância entre dois pontos na superfície da terra é mais complicado do
# simplesmente usar o Teorema de Pitágoras no plano. Seja tv1, gv1 e tv2 gv2 as latitudes e
# longitudes de dois pontos na superfície da terra. A distância em quilômetros entre estes dois
# pontos ao longo da superfície da terra é dada por:

#distancia = 6371.01 * arccos(sen(t v1) * sen(t v2) + cos(t v1) * cos(t v2) * cos(g v1 - g v2))

# Crie um programa Python que receba a latitude e a longitude de dois pontos na Terra em
# graus, calcule e exiba a distância entre eles em quilômetros ao longo da superfície.

import math #contas
import os #limpa tela
os.system('cls' if os.name == 'nt' else 'clear') #definicao de nome
import time #delay

print("DISTÂNCIA ENTRE DOIS PONTOS NA TERRA!")
print("(em caso de terraplanismo não utilize o programa)")

for i in range(3): #apenas estetica de espera 
    print('.')
    time.sleep(1) #reciclagem 
    
os.system('cls')

tv1 = float(input("Latitude do ponto 1: "))
gv1 = float(input("Longitude do ponto 1: "))
tv2 = float(input("Latitude do ponto 2: "))
gv2 = float(input("Longitude do ponto 2: "))

#conversão 
tv1 = math.radians(tv1)
gv1 = math.radians(gv1)
tv2 = math.radians(tv2)
gv2 = math.radians(gv2)

#formula fornecida
distancia = 6371.01 * math.acos(
    math.sin(tv1) * math.sin(tv2) +
    math.cos(tv1) * math.cos(tv2) * math.cos(gv1 - gv2)
)

print("Distancia entre os pontos ", distancia, "km")