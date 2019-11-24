import os
from kaa.sprites import Sprite
from kaa.geometry import Vector
from kaa.audio import Sound, Music
from kaa.fonts import Font

class AssetsController:

    def __init__(self):
        # Load all images:
        self.background_img = Sprite(os.path.join('assets', 'gfx', 'background.png'))
        self.player_img = Sprite(os.path.join('assets', 'gfx', 'player.png'))
        self.machine_gun_img = Sprite(os.path.join('assets', 'gfx', 'machine-gun.png'))
        self.force_gun_img = Sprite(os.path.join('assets', 'gfx', 'force-gun.png'))
        self.grenade_launcher_img = Sprite(os.path.join('assets', 'gfx', 'grenade-launcher.png'))
        self.machine_gun_bullet_img = Sprite(os.path.join('assets', 'gfx', 'machine-gun-bullet.png'))
        self.force_gun_bullet_img = Sprite(os.path.join('assets', 'gfx', 'force-gun-bullet.png'))
        self.grenade_launcher_bullet_img = Sprite(os.path.join('assets', 'gfx', 'grenade-launcher-bullet.png'))

        self.enemy_img = Sprite(os.path.join('assets', 'gfx', 'enemy.png'), frame_dimensions=Vector(33, 74),
                                frame_count=8, animation_frame_duration=50, animation_loop=True)
        self.enemy_stagger_img = Sprite(os.path.join('assets', 'gfx', 'enemy-stagger.png'))

        self.enemy_death_img = Sprite(os.path.join('assets','gfx','enemy-death.png'), frame_dimensions=Vector(103, 74),
                                      frame_count=9, animation_loop=False, animation_frame_duration=50)
        self.blood_splatter_img = Sprite(os.path.join('assets', 'gfx', 'blood-splatter.png'), frame_dimensions=Vector(50, 50),
                                      frame_count=7, animation_loop=False, animation_frame_duration=20)
        self.explosion_img = Sprite(os.path.join('assets', 'gfx', 'explosion.png'), frame_count=75,
                                    frame_dimensions=Vector(100,100), animation_frame_duration=12, animation_loop=False)

        # Load all sounds
        self.mg_shot_sound = Sound(os.path.join('assets', 'sfx', 'mg-shot.wav'))
        self.force_gun_shot_sound = Sound(os.path.join('assets', 'sfx', 'force-gun-shot.wav'))
        self.grenade_launcher_shot_sound = Sound(os.path.join('assets', 'sfx', 'grenade-launcher-shot.wav'))
        self.explosion_sound = Sound(os.path.join('assets', 'sfx', 'explosion.wav'))

        # Load all music tracks
        self.music_track_1 = Music(os.path.join('assets', 'music', 'track_1.wav'))

        # Load all fonts
        self.font_1 = Font(os.path.join('assets', 'fonts', 'paladise-script.ttf'))
        self.font_2 = Font(os.path.join('assets', 'fonts', 'DejaVuSans.ttf'))

