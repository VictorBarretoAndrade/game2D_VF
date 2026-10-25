import os

# Permite executar os testes do jogo sem abrir uma janela (ex.: em CI)
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
