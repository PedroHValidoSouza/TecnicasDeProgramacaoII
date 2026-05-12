import pytest
import Estacionamento

def test_CarroExibir():
    carroTest = Estacionamento.Carro("Test-la", "Tusca", "amarelo")
    assert carroTest.exibir() == "Carro Tusca da Test-la, de cor amarelo"

def test_FabricaObterCarro():
    carroTest = Estacionamento.Carro("Fiat", "Palio", "azul")
    carroTest1 = Estacionamento.fabricaCarro.obter_carro("Fiat", "Palio", "azul")
    assert carroTest1.exibir() == carroTest.exibir()

def test_FabricaOutput(capsys):
    Estacionamento.fabricaCarro.obter_carro("Volkswagen", "Fusca", "rosa")
    captured1 = capsys.readouterr()
    Estacionamento.fabricaCarro.obter_carro("Volkswagen", "Fusca", "rosa")
    captured2 = capsys.readouterr()
    assert captured1 != captured2
