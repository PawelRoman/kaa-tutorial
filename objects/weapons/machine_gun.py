import registry
import settings
from objects.bullets.machine_gun_bullet import MachineGunBullet
from objects.weapons.base import WeaponBase
from kaa.geometry import Vector


class MachineGun(WeaponBase):

    def __init__(self):
        # node's properties
        super().__init__(sprite=registry.global_controllers.assets_controller.machine_gun_img)

    def shoot_bullet(self):
        bullet_position = self.get_initial_bullet_position()
        bullet_velocity = Vector.from_angle_degrees(self.parent.rotation_degrees) * settings.MACHINE_GUN_BULLET_SPEED
        self.scene.space.add_child(MachineGunBullet(position=bullet_position, velocity=bullet_velocity,
                                                    rotation_degrees=self.parent.rotation_degrees))
        # reset cooldown time
        self.cooldown_time_remaining = self.get_cooldown_time()

        # play shooting sound
        registry.global_controllers.assets_controller.mg_shot_sound.play()

    def get_cooldown_time(self):
        return 100