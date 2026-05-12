
class Carro:

    def __init__(self, marca:str, modelo:str, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def exibir(self):
        return f'Carro {self.modelo} da {self.marca}, de cor {self.cor}'


class fabricaCarro:
    carros = {}

    @classmethod
    def obter_carro(cls, marca, modelo, cor):
        chave = (marca, modelo, cor)

        if chave not in cls.carros:
            cls.carros[chave] = Carro(marca, modelo, cor)
            print("> Novo tipo de carro registrado")
        
        return cls.carros[chave]


#vg significa vaga
carro_vg1 = fabricaCarro.obter_carro(
    "Volkswagen", "Fusca-1999", "amarela"
)

carro_vg2 = fabricaCarro.obter_carro(
    "Fiat", "Palio-2008", "cinza"
)

carro_vg3 = fabricaCarro.obter_carro(
    "Volkswagen", "Fusca-1999", "amarela"
)

print(">--------------------------") #separação

print(carro_vg1.exibir())
print(carro_vg2.exibir())
print(carro_vg3.exibir())