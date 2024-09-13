'''20. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.'''

area_pintada = float(input("Insira o tamanho da área a ser pintada em metros quadrados (m²): "))
area_pintada *= 1.10
cobertura_tinta = 6
tinta_necessaria = area_pintada / cobertura_tinta
lata_tamanho = 18 
lata_preco = 80.00  
galao_preco = 25.00 
latas_necessarias = tinta_necessaria // lata_tamanho


print(f"\nSituação 1: Apenas latas de 18 litros")
print('------------------------------------------')
print(f"\nSituação 2: Apenas galões de 3,6 litros")
print(f"Quantidade de galões necessários: {int()}")
print('------------------------------------------')
print(f"\nSituação 3: Mistura de latas e galões")
print(f"Quantidade de latas necessárias: {int()}")
print(f"Quantidade de galões necessários: {int()}")
print('------------------------------------------')



