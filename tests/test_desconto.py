from src.desconto import DescontoNormal


def test_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"
