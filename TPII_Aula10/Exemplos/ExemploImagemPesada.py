from abc import ABC, abstractmethod

class Imagem(ABC):
    @abstractmethod
    def exibir(self):
        pass

# Uma imagem Real'mente' pesada
class ImagemReal(Imagem):
    def __init__(self, nome_Arquivo):
        self.nome_arquivo = nome_Arquivo
        self.carregar_do_disco()
    
    def carregar_do_disco(self):
        print(f'-> Carregando {self.nome_arquivo} do disco...')

    def exibir(self):
        print(f'Exibindo {self.nome_arquivo}')

class ProxImagem(Imagem):
    def __init__(self, nome_Arquivo):
        self.nome_arquivo = nome_Arquivo
        self.imagem_Real = None

    def exibir(self):
        if self.imagemReal == None:
            self.imagem_Real = ImagemReal(self.nome_arquivo)
        self.imagem_Real.exibir()

Imagem = ProxImagem("fotoLinda.png")

print("Imagem criada")

Imagem.exibir()