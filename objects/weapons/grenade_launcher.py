import registry
from objects.weapons.base import WeaponBase


class GrenadeLauncher(WeaponBase):

    def __init__(self, position):
        # node's properties
        super().__init__(sprite=registry.global_controllers.assets_controller.grenade_launcher_img, position=position)
