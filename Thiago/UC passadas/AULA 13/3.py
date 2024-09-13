'''
3- Construa um algoritmo em PORTUGOL que leia dois valores numericos inteiros 
e efetue a adição; 
caso o resultado seja maior que 10, apresenta-lo.
'''

num1 = int(input('insira o primeiro numero: '))
num2 = int(input('insira o segundo numero: '))
soma = num1 + num2
if soma > 10:
    print(f"A soma dos valores é {soma}, que é maior que 10." )
