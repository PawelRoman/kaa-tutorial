import settings
from common.enums import WeaponType
from objects.player import Player
from kaa.geometry import Vector

class PlayerController:

    def __init__(self, scene):
        self.scene = scene
        self.player = Player(position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2))
        self.scene.root.add_child(self.player)

        self.player.change_weapon(WeaponType.MachineGun)