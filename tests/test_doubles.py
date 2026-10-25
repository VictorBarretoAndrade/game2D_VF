from src.desconto import Pedido
from tests.doubles import StubSemDesconto


def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100
