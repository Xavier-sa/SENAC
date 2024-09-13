import bombacombustivel
from bombacombustivel import BombaCombustivel
#!conceito de edit sem meus inputs
bomba = BombaCombustivel("DIESEL", 6.19, 15000) #igual o caminhao que abastece diariamente as bombas
                            #!tipo : preço : Quantidade na Bomba
                            
bomba.mostrar_quantidade_combustivel()  #?Quantidade que informei acima^

bomba.abastecer_por_valor(800)  #? Abastece em R$800 de Diesel os caminhoes

bomba.mostrar_quantidade_combustivel()  #! Mostra a quantidade restante de combustível

bomba.abastecer_por_litro(275)  #!Abastece 20 litros de DIESEL
bomba.mostrar_quantidade_combustivel()  #? Mostra a quantidade restante de combustível

bomba.alterar_valor(6.28)  #! Altera o valor do litro do diesel R$ 6.28
print(f"Novo valor do litro: R${bomba.valor_litro:.2f}")

bomba.alterar_combustivel("ALCOOL")  # Altera o tipo de combustível para Alcool
print(f"Novo tipo de combustível: {bomba.tipo_combustivel}")

bomba.alterar_quantidade_combustivel(14000)  #! Altera a quantidade de combustível para 1500 litros
bomba.mostrar_quantidade_combustivel()  #! Mostra a nova quantidade de combustível