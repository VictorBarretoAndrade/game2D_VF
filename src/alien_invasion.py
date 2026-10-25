import sys 
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)
        
        # Mudando a cor do plano de fundo em RGB
        self.bg_color = (self.settings.bg_color)
    
    
    def run_game(self):
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""
                
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: # Detecta quando uma tecla é pressionada
                    if event.key == pygame.K_RIGHT: # Verifica se a tecla pressionada é a seta para a direita
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT: # Verifica se a tecla pressionada é a seta para a esquerda
                        self.ship.moving_left = True
                
                elif event.type == pygame.KEYUP: # Detecta quando uma tecla é liberada
                    if event.key == pygame.K_RIGHT: # Verifica se a tecla liberada é a seta para a direita
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT: # Verifica se a tecla liberada é a seta para a esquerda
                        self.ship.moving_left = False

            # Redesenha a tela a cada passagem pelo laço
            self.screen.fill(self.bg_color)
            
            # Redesenha a nave em sua posição atual
            self.ship.blitme()
            
            # Atualiza a posição da nave com base na variável de controle
            self.ship.update() 

            # Torna visível a tela mais recente
            pygame.display.flip()
    
if __name__ == '__main__':
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
