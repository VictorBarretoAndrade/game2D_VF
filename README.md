# game2D_VF

Projeto realizado em aula durante a disciplina AQS (Alta Qualidade em Software).

Jogo 2D "Alien Invasion" desenvolvido em Python com Pygame: o jogador controla uma
nave na parte inferior da tela, move para os lados com as setas e atira com a barra
de espaço para destruir a frota de alienígenas.

## Como executar

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python src/alien_invasion.py
```

> Execute a partir da raiz do projeto para que as imagens da pasta `images` sejam encontradas.

## Análise estática

```bash
pip install -r requirements-dev.txt
ruff check .
ruff format .
cd src
mypy --strict .
```

## Estrutura (princípios SOLID)

| Arquivo | Responsabilidade |
| --- | --- |
| `src/alien_invasion.py` | Inicializa o jogo e executa o laço principal |
| `src/game_events.py` | `GameEventHandler`: trata eventos de teclado e janela |
| `src/bullet_manager.py` | `BulletManager`: cria, atualiza e remove projéteis |
| `src/fleet_manager.py` | `FleetManager`: cria e movimenta a frota de alienígenas |
| `src/game_renderer.py` | `GameRenderer`: desenha os elementos na tela |
| `src/alien.py` / `src/fast_alien.py` | Tipos de alienígena (extensão via herança - OCP) |
| `src/ship.py`, `src/bullet.py`, `src/settings.py` | Nave, projétil e configurações |
| `src/desconto.py` | Exemplo didático de desconto aplicando S, O, L, I e D |
