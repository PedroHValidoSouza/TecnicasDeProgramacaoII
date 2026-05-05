class DVDPlayer:
    def ligar(self):
        print("DVD ligado")

    def reproduzir(self):
        print("Reproduzindo DVD")

class Projetor:
    def ligar(self):
        print("Projetor ligado")
    
    def ajustar_resolucao(self):
        print("Resolução ajustada")

class SistemaSom:
    def ligar(self):
        print("Som ligado")
    
    def ajustar_volume(self):
        print('Volume ajustado')


class HomeTheterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projetor = Projetor()
        self.som = SistemaSom()

    def assistir_filme(self):
        print("Preparando para assistir filmes...")
        self.dvd.ligar()
        self.projetor.ligar()
        self.projetor.ajustar_resolucao()
        self.som.ligar()
        self.som.ajustar_volume()
        self.dvd.reproduzir()

home_Theter = HomeTheterFacade()
home_Theter.assistir_filme()
