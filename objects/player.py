from kaa.nodes import Node
from kaa.geometry import Vector
import registry
from common.enums import WeaponType
from objects.weapons.force_gun import ForceGun
from objects.weapons.grenade_launcher import GrenadeLauncher
from objects.weapons.machine_gun import MachineGun


class Player(Node):

    def __init__(self, position, hp=100):
        # node's properties
        super().__init__(z_index=10, sprite=registry.global_controllers.assets_controller.player_img, position=position)
        # custom properties
        self.hp = hp
        self.current_weapon = None
        self.change_weapon(WeaponType.MachineGun)

    def change_weapon(self, new_weapon):
        if self.current_weapon is not None:
            self.current_weapon.delete()  # delete the weapon's node from the scene
        if new_weapon == WeaponType.MachineGun:
            weapon = MachineGun(position=Vector(20, 0))  # position relative to the Player
        elif new_weapon == WeaponType.GrenadeLauncher:
            weapon = GrenadeLauncher(position=Vector(23, 0))
        elif new_weapon == WeaponType.ForceGun:
            weapon = ForceGun(position=Vector(27.5, 0))
        else:
            raise Exception('Unknown weapon type: {}'.format(new_weapon))
        self.add_child(weapon)  # add the weapon node as player's child node
        self.current_weapon = weapon  # remember the current weapon
