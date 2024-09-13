from bombacombustivel import BombaCombustivel#!
from devxavier import colors
from xavier import credenciais

def meu_menu():
    tipo_combustivel = input("Informe o tipo de combustível: ")
    valor_litro = float(input("Informe o valor por litro: "))
    quantidade_combustivel = float(input("Informe a quantidade de combustível inicial: "))

    
    bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)#invoco a class Bomba do meu outro arquivo

    
    while True:
        print(colors.YELLOW+ f'\n\t\tBomba Combustivel n: X1' + colors.END)
        print(colors.GREEN + f'\n\t\tMENU:\n\t\t' + colors.END)
        print(colors.GREEN + f'\t\t1. ABASTECER POR VALOR' + colors.END)
        print(colors.GREEN + f'\t\t2. ABASTECER POR LITRO' + colors.END)
        print(colors.GREEN + f'\t\t3. ALTERAR VALOR POR LITRO' + colors.END)
        print(colors.GREEN + f'\t\t4. ALTERAR TIPO DE COMBUSTIVEL' + colors.END)
        print(colors.GREEN + f'\t\t5. ALTERAR QUANTIDADE DE COMBUSTÍVEL' + colors.END)
        print(colors.GREEN + f'\t\t6. EXIBIR-qtd Combustivel' + colors.END)
        print(colors.GREEN + f'\t\t0. SAIR' + colors.END)
      
        print(colors.RED + f'\n\tlol\n\t\t' + colors.END)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Quanto em R$ deseja abastecer?: "))
            bomba.abastecer_por_valor(valor)
        elif opcao == '2':
            litros = float(input("Qtd de Litros?: "))
            bomba.abastecer_por_litro(litros)
        elif opcao == '3':
            novo_valor = float(input("Atualizando o preço do litro!\nNovo valor por litro: "))
            bomba.alterar_valor(novo_valor)
        elif opcao == '4':
            novo_combustivel = input("Informe o novo tipo de combustível: ")
            bomba.alterar_combustivel(novo_combustivel)
        elif opcao == '5':
            nova_quantidade = float(input("Informe a nova quantidade de combustível: "))
            bomba.alterar_quantidade_combustivel(nova_quantidade)
        elif opcao == '6':
            bomba.mostrar_quantidade_combustivel()
        elif opcao == '0':
            credenciais()#!de tanto errar aprendi kkk
            "vou treina isso ao finalizar algo"
            break                
        else:
            
            print(colors.RED + f'Opção inválida. Tente novamente' + colors.END)

meu_menu()
