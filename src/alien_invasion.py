import sys
import pygame


class AlienInvasion:
    """Classe principal para gerenciamento do jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos do jogo."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Criando um laço de repetição para a tela sempre ficar visível até que
        o usuário decida fechar a janela."""
        while True:
            # "ouvindo" algum evento no mouse ou teclado.
            # para acessa aos eventos que o Pygame detecta, só chamar o método event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # encerra o jogo.

            # Tornando visível a tela desenhada recentemente
            pygame.display.flip()


if __name__ == '__main__':
    # Fazendo uma instância da classe.
    alien_invasion = AlienInvasion()
    # Após instanciar um objeto, ele pode realizar a chamada de seus comportamentos.
    # Nesse momento, ele vamos chamar o run_game.
    alien_invasion.run_game()
