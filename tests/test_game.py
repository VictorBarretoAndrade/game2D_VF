import pygame
import pytest

from src.alien import Alien
from src.bullet import Bullet
from src.fast_alien import FastAlien
from src.fleet_manager import FleetManager
from src.settings import Settings
from src.ship import Ship


@pytest.fixture
def settings():
    return Settings()


@pytest.fixture
def screen(settings):
    pygame.init()
    return pygame.display.set_mode((settings.screen_width, settings.screen_height))


@pytest.fixture
def ship(screen, settings):
    return Ship(screen, settings)


def test_ship_move_esquerda(ship):
    x_inicial = ship.x

    ship.moving_left = True
    ship.update()

    assert ship.x < x_inicial


def test_ship_nao_sai_da_tela_pela_direita(ship, screen):
    ship.rect.right = screen.get_rect().right
    ship.x = float(ship.rect.x)
    x_inicial = ship.x

    ship.moving_right = True
    ship.update()

    assert ship.x == x_inicial


def test_bullet_move_para_cima(screen, settings, ship):
    bullet = Bullet(screen, settings, ship)
    y_inicial = bullet.y

    bullet.update()

    assert bullet.y == y_inicial - settings.bullet_speed


def test_alien_detecta_borda_direita(screen, settings):
    alien = Alien(screen, settings)
    alien.rect.right = screen.get_rect().right

    assert alien.check_edges() is True


def test_alien_longe_da_borda(screen, settings):
    alien = Alien(screen, settings)
    alien.rect.centerx = screen.get_rect().centerx

    assert alien.check_edges() is False


@pytest.mark.parametrize("alien_class, multiplicador", [(Alien, 1), (FastAlien, 2)])
def test_velocidade_dos_tipos_de_alien(screen, settings, alien_class, multiplicador):
    alien = alien_class(screen, settings)
    x_inicial = alien.x

    alien.update()

    assert alien.x == pytest.approx(x_inicial + settings.alien_speed * multiplicador)


def test_fleet_manager_cria_frota_com_tipo_informado(screen, settings, ship):
    fleet_manager = FleetManager(screen, settings, ship, FastAlien)

    fleet_manager.create_fleet()

    assert len(fleet_manager.aliens) > 0
    assert all(isinstance(alien, FastAlien) for alien in fleet_manager.aliens)


def test_mudar_direcao_da_frota(screen, settings, ship):
    fleet_manager = FleetManager(screen, settings, ship)
    fleet_manager.create_fleet()
    alien = fleet_manager.aliens.sprites()[0]
    y_inicial = alien.rect.y

    fleet_manager._change_fleet_direction()

    assert settings.fleet_direction == -1
    assert alien.rect.y == y_inicial + settings.fleet_drop_speed
