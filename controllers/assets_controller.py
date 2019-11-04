import os
from kaa.sprites import Sprite
from kaa.geometry import Vector


class AssetsController:

    def __init__(self):
        # Load all images:
        self.player_img = Sprite(os.path.join('assets', 'gfx', 'player.png'))
        self.machine_gun_img = Sprite(os.path.join('assets', 'gfx', 'machine-gun.png'))
        self.force_gun_img = Sprite(os.path.join('assets', 'gfx', 'force-gun.png'))
        self.grenade_launcher_img = Sprite(os.path.join('assets', 'gfx', 'grenade-launcher.png'))
        self.machine_gun_bullet_img = Sprite(os.path.join('assets', 'gfx', 'machine-gun-bullet.png'))
        self.force_gun_bullet_img = Sprite(os.path.join('assets', 'gfx', 'force-gun-bullet.png'))
        self.grenade_launcher_bullet_img = Sprite(os.path.join('assets', 'gfx', 'grenade-launcher-bullet.png'))
        # enemy image has two frames, first frame shows normal stance and second frame
        # is to show a 'stagger' state when enemy takes a hit
        self.enemy_img = Sprite(os.path.join('assets','gfx','enemy.png'), frame_dimensions=Vector(50, 50), frame_count=2)

