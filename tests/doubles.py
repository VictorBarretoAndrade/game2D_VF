from src.alien import Alien
from src.desconto import IDesconto


class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0


class StubAlienNaBorda(Alien):
    """Stub de alienígena que sempre informa estar na borda da tela."""

    def check_edges(self):
        return True
