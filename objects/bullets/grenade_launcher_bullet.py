import random
from kaa.physics import BodyNodeType, HitboxNode, BodyNode
from kaa.geometry import Circle
import registry
import settings
from common.enums import HitboxMask


class GrenadeLauncherBullet(BodyNode):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.grenade_launcher_bullet_img,
                         z_index=30,
                         body_type=BodyNodeType.kinematic,  # as we want to handle collision effects on our own
                         lifetime=5000,  # will be removed from the scene automatically after 5 secs
                         rotation_degrees=random.uniform(0, 360),  # a random rotation between 0 and 360 degs
                         *args, **kwargs)
        self.add_child(HitboxNode(shape=Circle(radius=6),  # circular hitbox
              mask=HitboxMask.bullet,  # we are bullet
              collision_mask=HitboxMask.enemy,  # want to collide with objects whose mask is enemy
              trigger_id=settings.COLLISION_TRIGGER_GRENADE_LAUNCHER_BULLET  # used when registering collision handler function
              ))

