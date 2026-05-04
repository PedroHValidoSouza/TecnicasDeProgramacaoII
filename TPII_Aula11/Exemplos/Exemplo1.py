from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

class Arquivo(Item):
    def __init__(self, nome):
        self.nome = nome
        self.Intnl = ''

    def mostrar(self, nivel=0):
        for i in range(max(1, nivel)):
            self.Intnl += '  '
        print(F"{self.Intnl}↳ {self.nome}")

class Pasta(Item):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []
        self.Intnl = ''

    def adicionar(self, Item):
        self.itens.append(Item)
    
    def mostrar(self, nivel=0):

        for i in range(max(1, nivel)):
            self.Intnl += '  '
        print(F"{self.Intnl}↳ {self.nome}:")
        for item in self.itens:
            item.mostrar(nivel + 1)

root = Pasta("Root")
docs = Pasta("documentos")
imgs = Pasta("imagens")

docs.adicionar(Arquivo("Pi-2026.pdf"))
docs.adicionar(Arquivo("relatorioMaio.docx"))

imgs.adicionar(Arquivo('Foto.png'))
root.adicionar(docs)
root.adicionar(imgs)

root.mostrar()
