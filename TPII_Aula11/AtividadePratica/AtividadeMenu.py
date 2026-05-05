from abc import ABC, abstractmethod

class ItemMenu(ABC):
    @abstractmethod
    def get_Preco():
        pass

class Prato(ItemMenu):
    # O prato tem nome e preco
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def get_Preco(self):
        return self.preco
    
    def get_Nome(self):
        return self.nome

class Combo(ItemMenu):
    # Aqui alem do nome e a lista dos pratos
    #  resolvi colocar o desconto(já que normalmente combos tem um desconto)
    def __init__(self, nome, desconto: float = 10):
        self.nome = nome
        self.pratos = []
        self.desconto = desconto
    
    def add_Prato(self, Prato):
        self.pratos.append(Prato)
    
    # calcula-se o preco total e desconta a porcentagem lá de cima
    def get_Preco(self):
        if len(self.pratos) > 0:
            preco = 0
            for prato in self.pratos:
                preco += prato.get_Preco()
            preco *= (100 - self.desconto)/100
            return preco
        else:
            raise ValueError("NoPratesFound404")
    
    # Imprime o combo
    def get_Combo(self):
        if len(self.pratos) > 0:
            raise ValueError("NoPratesFound404")
        texto = f'|Combo: {self.nome}\n'
        for prato in self.pratos:
            texto += f"|> {prato.get_Nome()}\n"
        texto += f'|Preço: {self.get_Preco(): .2f}'
        return texto

BatataFrita = Prato("Batata frita s/ sal", 14.90)
HotDog = Prato("Cachorro quente com purê", 19.99)
SucoLaranjaMedio = Prato("Suco de laranja 600ml c/ açucar", 15.40)
BoloChocolate = Prato("Fatia de bolo de chocolate c/ cobertura", 12.20)

ComboDelirio = Combo("Delirio de sabado")
ComboDelirio.add_Prato(BatataFrita)
ComboDelirio.add_Prato(HotDog)
ComboDelirio.add_Prato(SucoLaranjaMedio)
ComboDelirio.add_Prato(BoloChocolate)

print(ComboDelirio.get_Combo())