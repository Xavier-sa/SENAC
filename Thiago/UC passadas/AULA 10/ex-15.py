'''15. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de
venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um
percentual informado pelo usuário.'''

preco_custo = float(input("Insira o preço de custo do produto: R$ "))
percentual_acrescimo = float(input("Insira o percentual de acréscimo (%): "))
acrescimo = preco_custo * (percentual_acrescimo / 100)
valor_venda = preco_custo + acrescimo
print(f"O valor de venda do produto é: R$ {valor_venda:.2f}")

