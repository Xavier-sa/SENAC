'''14. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem
juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das
prestações.'''

valor_compra = float(input("Insira o valor total da compra: R$ "))
num_parcelas = 5
valor_prestacao = valor_compra / num_parcelas
print(f"O valor de cada prestação (em 5 parcelas sem juros) é: R$ {valor_prestacao:.2f}")

