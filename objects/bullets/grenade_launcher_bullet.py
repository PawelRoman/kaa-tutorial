import random
from kaa.nodes import Node
from kaa.physics import BodyNodeType, HitboxNode
from kaa.geometry import Vector, Circle

import registry
import settings
from common.enums import HitboxMask


class GrenadeLauncherBullet(Node):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.grenade_launcher_bullet_img,
                         z_index=30,
                         body_type=BodyNodeType.kinematic,  # as we want to handle collision effects on our own
                         lifetime=5000, # will be removed from the scene automatically after 5 secs
                         angular_velocity_degrees=random.uniform(-3,3), # make it rotate as it's flying
                         *args, **kwargs)
        self.add_child(HitboxNode(shape=Circle(radius=6),  # circular hitbox
                                  mask=HitboxMask.bullet,  # we are bullet
                                  collision_mask=HitboxMask.enemy,  # want to collide with objects whose mask is enemy
                                  trigger_id=settings.COLLISION_TRIGGER_GRENADE_LAUNCHER_BULLET  # used when registering collision handler function
                                  ))

