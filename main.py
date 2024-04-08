class BombaCombustivel:

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            print(f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
            self.quantidade_combustivel -= litros_abastecidos
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecer_por_litro(self, litros):

        if litros <= 0:
            print("Quantidade inválida.")
            return
        valor_a_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")
            self.quantidade_combustivel -= litros
        else:
            print("Não há combustível suficiente na bomba.")

    def alterar_valor(self, novo_valor):

        if novo_valor <= 0:
            print("Valor inválido.")
            return
        self.valor_litro = novo_valor
        print(f"Valor do litro de {self.tipo_combustivel} alterado para R$ {novo_valor:.2f}")

    def alterar_combustivel(self, novo_combustivel):

        self.tipo_combustivel = novo_combustivel
        print(f"Tipo de combustível alterado para {novo_combustivel}.")

    def alterar_quantidade_combustivel(self, nova_quantidade):

        if nova_quantidade < 0:
            print("Quantidade inválida.")
            return
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível atualizada para {nova_quantidade:.2f} litros.")



bomba1 = BombaCombustivel("Gasolina", 5.00, 1000)

bomba1.abastecer_por_valor(50)  
bomba1.abastecer_por_litro(20)  
bomba1.alterar_valor(4.80)  
bomba1.alterar_combustivel("Etanol")  
bomba1.alterar_quantidade_combustivel(1500)  
