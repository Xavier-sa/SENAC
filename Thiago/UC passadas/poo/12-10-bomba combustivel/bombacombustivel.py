"""Classe Bomba de Combustível: 
Faça um programa completo utilizando classes e métodos que:
    Possua uma classe chamada BombaCombustível, com no mínimo esses atributos:
                                        tipoCombustivel.
                                        valorLitro
                                        quantidadeCombustivel
Possua no mínimo esses métodos:
                    abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
                    
                    abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
                    
                    alterarValor( )  – altera o valor do litro do combustível.
                                        
                    alterarCombustivel( ) – altera o tipo do combustível.
                                        
                    alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.


OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade
de combustível total na bomba."""


 
class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")
    
    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Valor a pagar: R${valor_pagar:.2f}")
        else:
            print("Não há combustível suficiente na bomba.")
    
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
    
    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
    
    def mostrar_quantidade_combustivel(self):
        print(f"Quantidade de combustível na bomba: {self.quantidade_combustivel:.2f} litros")


