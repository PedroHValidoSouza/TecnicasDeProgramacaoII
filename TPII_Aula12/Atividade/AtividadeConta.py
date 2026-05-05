
class ContaBancaria:
    def __init__(self, saldo: int = 100):
        self.Saldo = saldo

    def get_Saldo(self):
        return self.Saldo
    
    def add_Saldo(self, moreSaldo):
        self.Saldo += moreSaldo

class Emprestimo:
    def Realizar_Emprestimo(self, quant: int):
        quantia = quant
        return quantia

class Seguranca():

    def __init__(self, senha):
        self.senha = senha
    
    def insert_senha(self, senhaInserida):
        if senhaInserida == self.senha:
            return True
        else:
            return False


class FacadeSistemaBancario():
    def __init__(self):
        self.seguranca = Seguranca(1234)
        self.emprestimo = Emprestimo()
        self.conta = ContaBancaria()
    
    def realizar_transacao(self, senha: int):
        if self.seguranca.insert_senha(senha):
            val = self.emprestimo.Realizar_Emprestimo(100)
            self.conta.add_Saldo(val)
            return "Emprestimo realizado"
        else:
            return "Senha incorreta"
    
    def get_Saldo(self):
        return self.conta.get_Saldo()

ContaNoBanco = FacadeSistemaBancario()

print(ContaNoBanco.get_Saldo())

ContaNoBanco.realizar_transacao(1234)

print("-----------")

print(ContaNoBanco.get_Saldo())

