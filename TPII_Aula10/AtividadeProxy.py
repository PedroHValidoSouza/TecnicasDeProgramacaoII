from abc import ABC, abstractmethod
import random

# Interface de serviço
class Servico(ABC):
    @abstractmethod
    def executar(self):
        pass

# Classe concreta muito importante
class ServicoMuitoImportante(Servico):
    def executar(self):
        # Uma graçinha: ele gera uma chave aleatoria só para simular um processo
        self.passKey = random.randint(1000, 9999)
        return(f"Chave de acesso: {self.passKey}")


# A classe de proxy
class ProxyServico(Servico):
    def __init__(self):
        self.servico = ServicoMuitoImportante
        self.usos = 3 # a quantidade de usos
    
    def executar(self):
        if self.usos <= 0:
            # Caso seja 0, o sistema barra
            return "Limite de usos atingido, pague R$ 999,90 para continuar."
        else:
            self.usos -= 1
            return (self.servico.executar(self))

servico1 = ProxyServico()

# Usei o range(loop) 4 vezes
for i in range(4):
    print(servico1.executar())