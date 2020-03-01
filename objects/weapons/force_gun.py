import registry
import settings
from objects.bullets.force_gun_bullet import ForceGunBullet
from objects.weapons.base import WeaponBase
from kaa.geometry import Vector

class ForceGun(WeaponBase):

    def __init__(self):
        # node's properties
        super().__init__(sprite=registry.global_controllers.assets_controller.force_gun_img)

    def shoot_bullet(self):
        bullet_position = self.get_initial_bullet_position()
        bullet_velocity = Vector.from_angle_degrees(self.parent.rotation_degrees) * settings.FORCE_GUN_BULLET_SPEED
        self.scene.space.add_child(ForceGunBullet(position=bullet_position, velocity=bullet_velocity))
        # reset cooldown time
        self.cooldown_time_remaining =  self.get_cooldown_time()
        # play shooting sound
        registry.global_controllers.assets_controller.force_gun_shot_sound.play()

    def get_cooldown_time(self):
        return 250