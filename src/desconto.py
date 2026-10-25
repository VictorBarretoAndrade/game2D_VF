from abc import ABC, abstractmethod


# Classe abstrata que define o contrato para todos os tipos de desconto
class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


# Implementação para cliente normal
class DescontoNormal(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


# Implementação para cliente VIP
class DescontoVIP(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2


# Implementação para cliente Premium
class DescontoPremium(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3


# LSP: qualquer subclasse de Desconto pode substituir a classe pai sem quebrar o programa
def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)


def main() -> None:
    valor = 100

    print("Normal:", aplicar_desconto(DescontoNormal(), valor))
    print("VIP:", aplicar_desconto(DescontoVIP(), valor))
    print("Premium:", aplicar_desconto(DescontoPremium(), valor))


if __name__ == "__main__":
    main()
