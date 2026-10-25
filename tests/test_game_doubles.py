import pygame
import pytest

from src.fleet_manager import FleetManager
from src.game_events import GameEventHandler
from src.settings import Settings
from src.ship import Ship
from tests.doubles import StubAlienNaBorda


@pytest.fixture
def settings():
    return Settings()


@pytest.fixture
def screen(settings):
    pygame.init()
    return pygame.display.set_mode((settings.screen_width, settings.screen_height))


def test_frota_muda_direcao_com_stub_na_borda(screen, settings):
    ship = Ship(screen, settings)
    fleet_manager = FleetManager(screen, settings, ship, StubAlienNaBorda)
    fleet_manager.create_fleet()

    fleet_manager._check_fleet_edges()

    assert settings.fleet_direction == -1


def test_barra_de_espaco_dispara_projetil_com_mock(mocker):
    mock_ship = mocker.Mock()
    mock_bullet_manager = mocker.Mock()
    event_handler = GameEventHandler(mock_ship, mock_bullet_manager)
    evento = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)

    event_handler._handle_keydown(evento)

    mock_bullet_manager._fire_bullet.assert_called_once()


def test_seta_direita_move_nave_com_mock(mocker):
    mock_ship = mocker.Mock(moving_right=False)
    mock_bullet_manager = mocker.Mock()
    event_handler = GameEventHandler(mock_ship, mock_bullet_manager)

    event_handler._handle_keydown(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))

    assert mock_ship.moving_right is True
    mock_bullet_manager._fire_bullet.assert_not_called()


def test_colisao_da_nave_encerra_o_jogo(screen, settings, mocker):
    ship = Ship(screen, settings)
    fleet_manager = FleetManager(screen, settings, ship)
    mocker.patch("pygame.sprite.spritecollideany", return_value=True)

    with pytest.raises(SystemExit):
        fleet_manager._check_ship_collision()
