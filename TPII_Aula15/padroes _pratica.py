from abc import ABC, abstractmethod


# =====================================================
# FACTORY METHOD
# =====================================================

# Classe abstrata de pagamento
class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass


# Pagamento com cartão
class PagamentoCartao(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com CARTÃO.")

# Pagamento com boleto
class PagamentoBoleto(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} no BOLETO.")


# Pagamento com PIX
class PagamentoPix(Pagamento):

    def pagar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado com PIX.")


# Factory Method
class FabricaPagamento:

    @staticmethod
    def criar_pagamento(tipo):

        if tipo == "cartao":
            return PagamentoCartao()

        elif tipo == "pix":
            return PagamentoPix()

        elif tipo == "boleto":
            return PagamentoBoleto()
        
        else:
            raise ValueError("Tipo de pagamento inválido.")


# =====================================================
# CHAIN OF RESPONSIBILITY
# =====================================================

# Classe base dos validadores
class Validador:

    def __init__(self):
        self.proximo = None

    def definir_proximo(self, proximo):
        self.proximo = proximo
        return proximo

    def processar(self, pedido):

        if self.proximo:
            return self.proximo.processar(pedido)

        return True


# Verifica estoque
class ValidarEstoque(Validador):

    def processar(self, pedido):

        if pedido["estoque"] <= 0:
            print("Produto sem estoque.")
            return False

        print("Estoque validado.")
        return super().processar(pedido)


# Verifica valor mínimo
class ValidarValorMinimo(Validador):

    def processar(self, pedido):

        if pedido["valor"] < 10:
            print("Pedido abaixo do valor mínimo.")
            return False

        print("Valor mínimo validado.")
        return super().processar(pedido)


# Verifica CPF
class ValidarCPF(Validador):

    def processar(self, pedido):

        if ValidacaoDeCPF(pedido["cpf"]):
            print("CPF validado.")
            return super().processar(pedido)
        else:
            print("CPF invalidado.")


def ValidacaoDeCPF(cpf):
    if len(cpf) != 11:
        return False
    
    Caracteres = []
    for i in range(11):
        Caracteres.append(int(cpf[i]))
    
    somDig1 = 0
    for i in range(9):
        somDig1 += (Caracteres[i] * (10 - i))
    somDig1 *= 10
    dig1 = somDig1 % 11

    if dig1 != Caracteres[9]:
        return False
    

    somDig2 = 0
    for i in range(10):
        somDig2 += (Caracteres[i] * (11 - i))
    somDig2 *= 10
    dig2 = somDig2 % 11

    if dig2 != Caracteres[10]:
        return False
    else:
        return True

# =====================================================
# FACADE
# =====================================================

class SistemaPedido:

    def finalizar_pedido(self, pedido, tipo_pagamento):

        print("Iniciando pedido...\n")

        # Criando a cadeia de validação
        estoque = ValidarEstoque()
        valor = ValidarValorMinimo()
        cpf = ValidarCPF()

        estoque.definir_proximo(valor).definir_proximo(cpf)

        # Executando validações
        if estoque.processar(pedido):

            print("\nPedido aprovado.")

            pagamento = FabricaPagamento.criar_pagamento(
                tipo_pagamento
            )

            pagamento.pagar(pedido["valor"])

            print("Pedido finalizado com sucesso.")

        else:
            print("\nPedido cancelado.")


# =====================================================
# EXECUÇÃO
# =====================================================

pedido = {
    "valor": 150,
    "estoque": 10,
    "cpf": "52998224725"
}

sistema = SistemaPedido()

sistema.finalizar_pedido(
    pedido,
    "boleto"
)
