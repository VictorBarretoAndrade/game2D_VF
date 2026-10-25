import abc


# ISP: interfaces específicas em vez de uma interface genérica
class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        raise NotImplementedError


class ICupom(abc.ABC):
    @abc.abstractmethod
    def aplicar_cupom(self, codigo: str) -> bool:
        raise NotImplementedError


class IVIP(abc.ABC):
    @abc.abstractmethod
    def validar_usuario_vip(self, usuario: str) -> bool:
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


# Apenas o cliente VIP implementa cupom e validação VIP
class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor: float) -> float:
        return valor * 0.2

    def aplicar_cupom(self, codigo: str) -> bool:
        return True

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario == "vip"


class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3


# LSP: qualquer implementação de IDesconto pode ser usada sem quebrar o programa
def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)


def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)


# DIP: Pedido depende da abstração IDesconto, e não de uma implementação concreta
class Pedido:
    def __init__(self, desconto: IDesconto) -> None:
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)


def main() -> None:
    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())
    pedido_premium = Pedido(DescontoPremium())

    print("Normal:", pedido_normal.total(valor))
    print("VIP:", pedido_vip.total(valor))
    print("Premium:", pedido_premium.total(valor))

    print("Cupom VIP:", aplicar_cupom(DescontoVIP(), "DESC10"))


if __name__ == "__main__":  # pragma: no cover
    main()
