import os
from kaa.sprites import Sprite


class AssetsController:

    def __init__(self):
        # Images
        self.player_img = Sprite(os.path.join('assets', 'gfx', 'player.png'))
