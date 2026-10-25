class Settings:
    """Classe que armazena todas as configurações do jogo."""
    
    def __init__(self):
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Cor de fundo (cinza claro)
        self.ship_speed = 1.5 # Velocidade da nave
