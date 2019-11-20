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
        self.enemy_death_img = Sprite(os.path.join('assets','gfx','enemy-death.png'), frame_dimensions=Vector(70, 50),
                                      frame_count=8, animation_loop=False, animation_frame_duration=20)
        self.blood_splatter_img = Sprite(os.path.join('assets', 'gfx', 'blood-splatter.png'), frame_dimensions=Vector(50, 50),
                                      frame_count=7, animation_loop=False, animation_frame_duration=20)
        self.explosion_img = Sprite(os.path.join('assets', 'gfx', 'explosion.png'), frame_count=75,
                                    frame_dimensions=Vector(100,100), animation_frame_duration=12, animation_loop=False)

