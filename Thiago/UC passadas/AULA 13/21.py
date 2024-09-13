'''
21. Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e
ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70
anos podem adquirir apólices de seguro. Quanto às classes de ocupações, foram
definidos três grupos de risco. A tabela abaixo fornece as categorias em função da
faixa etária e do grupo de risco. Dados nome, idade e grupo de risco, determinar a
categoria do pretendente à aquisição de tal seguro. Imprimir o nome a idade e a
categoria do pretendente, e , caso a idade não esteja na faixa necessária, imprimir uma
mensagem.'''


nome = input("Digite o nome do pretendente: ")
idade = int(input("Digite a idade do pretendente: "))
grupo_risco = input("Digite o grupo de risco (Baixo, Medio ou Alto): ")

match  (grupo_risco):
    case 17:
        print('Baixo')
    case 18:
        print('Medio')
   
#nao consegui concluir