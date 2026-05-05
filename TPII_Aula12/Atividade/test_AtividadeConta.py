from AtividadeConta import ContaNoBanco
import pytest

def test_SaldoMudou():

    ContaNoBanco.realizar_transacao(1234)
    assert ContaNoBanco.get_Saldo == 200