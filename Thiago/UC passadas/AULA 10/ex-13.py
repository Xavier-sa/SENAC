
'''13. Faça um algoritmo que receba um valor que foi depositado e exiba o valor com
rendimento após um mês.
Considere fixo o juro da poupança em 0,70% a. m'''

valor_depositado = float(input("Insira o valor depositado: R$ "))
juro_poupanca = 0.007  # 0,70% convertido para decimal (0,007)
rendimento = valor_depositado * juro_poupanca
valor_final = valor_depositado + rendimento

print(f"\nValor depositado: R$ {valor_depositado:.2f}")
print(f"Rendimento após um mês: R$ {rendimento:.2f}")
print(f"Valor final após um mês: R$ {valor_final:.2f}")


