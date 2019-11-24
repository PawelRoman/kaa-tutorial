import registry
import settings
import random
from objects.bullets.grenade_launcher_bullet import GrenadeLauncherBullet
from objects.weapons.base import WeaponBase
from kaa.geometry import Vector


class GrenadeLauncher(WeaponBase):

    def __init__(self, position):
        # node's properties
        super().__init__(sprite=registry.global_controllers.assets_controller.grenade_launcher_img, position=position)

    def shoot_bullet(self):
        bullet_position = self.get_initial_bullet_position()
        bullet_velocity = Vector.from_angle_degrees(self.parent.rotation_degrees) * settings.GRENADE_LAUNCHER_BULLET_SPEED
        self.scene.space.add_child(GrenadeLauncherBullet(position=bullet_position, velocity=bullet_velocity))
        # reset cooldown time
        self.cooldown_time_remaining =  self.get_cooldown_time()
        # play shooting sound
        registry.global_controllers.assets_controller.grenade_launcher_shot_sound.play()


    def get_cooldown_time(self):
        return 1000