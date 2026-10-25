import pygame
from pygame.sprite import Sprite

from settings import Settings


class Alien(Sprite):
    """Gerencia os alienígenas."""

    def __init__(
        self, alien_invasion_screen: pygame.Surface, alien_invasion_settings: Settings
    ) -> None:
        """Inicializa o alienígena e define sua posição inicial."""
        # Chama o construtor da classe Sprite para inicializar o alienígena como um sprite
        super().__init__()
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings

        # Carrega a imagem do alienígena e obtém seu rect
        self.image: pygame.Surface = pygame.image.load("images/alien.bmp")
        self.rect: pygame.Rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal como float para permitir movimentos suaves
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def drawme(self) -> None:
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)  # ('o que', 'onde')

    def update(self) -> None:
        """Move o alienígena para a direita ou esquerda conforme a direção da frota."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self) -> bool:
        """Retorna True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
