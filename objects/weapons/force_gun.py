import registry
from objects.weapons.base import WeaponBase


class ForceGun(WeaponBase):

    def __init__(self, position):
        # node's properties
        super().__init__(sprite=registry.global_controllers.assets_controller.force_gun_img, position=position)
