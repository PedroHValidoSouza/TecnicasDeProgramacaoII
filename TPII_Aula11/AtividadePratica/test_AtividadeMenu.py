from AtividadeMenu import BatataFrita, ComboDelirio, Combo, Prato
import pytest

def test_Preco_Prato():
    assert BatataFrita.get_Preco() == 14.90

def test_Preco_Combo():
    assert f'{ComboDelirio.get_Preco()}: .2f' == '56.24'

def test_Combo_Vazio():
    with pytest.raises(ValueError, match="NoPrates"):
        ComboT = Combo("Combo Teste")
        ComboT.get_Preco()