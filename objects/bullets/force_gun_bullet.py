import random
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Circle
import registry
import settings
from common.enums import HitboxMask


class ForceGunBullet(BodyNode):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.force_gun_bullet_img,
                         z_index=30,
                         body_type=BodyNodeType.dynamic,
                         mass=random.uniform(0.5, 8),  # a random mass,
                         lifetime=10000, # will be removed from the scene automatically after 10 secs
                         *args, **kwargs)
        self.add_child(HitboxNode(shape=Circle(radius=10),
                                  mask=HitboxMask.bullet,
                                  collision_mask=HitboxMask.all,
                                  trigger_id=settings.COLLISION_TRIGGER_FORCE_GUN_BULLET))
