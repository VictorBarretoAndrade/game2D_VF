class Settings:
    """Classe que armazena todas as configurações do jogo."""

    def __init__(self):
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Cor de fundo (cinza claro)
        self.ship_speed = 1.5  # Velocidade da nave

        # Configurações dos projéteis
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 1  # Máximo de projéteis na tela ao mesmo tempo

        # Configurações do alien
        self.alien_speed = 0.3
        self.fleet_drop_speed = 10  # Velocidade de descida da frota
        self.fleet_direction = 1  # 1 representa a direita; -1 representa a esquerda
