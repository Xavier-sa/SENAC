'''10. Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a
variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor
da variável A. Apresentar os valores trocados.'''

A = input("Insira o valor para a variável A: ")
B = input("Insira o valor para a variável B: ")
A, B = B, A
print(f"Após a troca, o valor de A é: {A}")
print(f"Após a troca, o valor de B é: {B}")

