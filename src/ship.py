import pygame


class Ship:
    """Gerencia a nave espacial."""

    def __init__(self, alien_invasion_screen, alien_invasion_settings):
        """Inicializa a nave e define sua posição inicial."""
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        # Rect é uma estrutura usada para representar posições e áreas retangulares
        self.screen_rect = self.screen.get_rect()

        # Carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Posiciona a nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Variáveis de controle de movimento da nave
        self.moving_right = False
        self.moving_left = False

        # Armazena a posição horizontal como float para permitir movimentos suaves
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha a nave em sua posição atual."""
        self.screen.blit(self.image, self.rect)  # ('o que', 'onde')

    def update(self):
        """Atualiza a posição da nave com base nas variáveis de controle."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Atualiza o rect da nave
        self.rect.x = self.x
