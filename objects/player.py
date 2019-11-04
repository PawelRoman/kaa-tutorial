from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Vector, Polygon
import registry
import settings
from common.enums import WeaponType, HitboxMask
from objects.weapons.force_gun import ForceGun
from objects.weapons.grenade_launcher import GrenadeLauncher
from objects.weapons.machine_gun import MachineGun
from kaa.colors import Color


class Player(BodyNode):

    def __init__(self, position, hp=100):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic, mass=1,
                         z_index=10, sprite=registry.global_controllers.assets_controller.player_img, position=position)
        # create a hitbox and add it as a child node to the Player
        self.add_child(HitboxNode(
            shape=Polygon([Vector(-8, -19), Vector(8, -19), Vector(8, 19), Vector(-8, 19), Vector(-8, -19)]),
            mask=HitboxMask.player,
            collision_mask=HitboxMask.enemy,
            trigger_id=settings.COLLISION_TRIGGER_PLAYER,
        ))
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

    def cycle_weapons(self):
        if self.current_weapon is None:
            return
        elif isinstance(self.current_weapon, MachineGun):
            self.change_weapon(WeaponType.GrenadeLauncher)
        elif isinstance(self.current_weapon, GrenadeLauncher):
            self.change_weapon(WeaponType.ForceGun)
        elif isinstance(self.current_weapon, ForceGun):
            self.change_weapon(WeaponType.MachineGun)
