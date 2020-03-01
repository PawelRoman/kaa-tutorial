import random
import registry
import settings
from kaa.physics import BodyNode, BodyNodeType, HitboxNode
from kaa.geometry import Polygon, Vector
from common.enums import HitboxMask


class MachineGunBullet(BodyNode):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.machine_gun_bullet_img,
                         z_index=30,
                         body_type=BodyNodeType.kinematic,  # MG bullets are kinematic bodies
                         lifetime=3000,  # will be removed from the scene automatically after 3 secs
                         *args, **kwargs)
        self.add_child(
            HitboxNode(shape=Polygon([Vector(-13, -4), Vector(13, -4), Vector(13, 4), Vector(-13, 4), Vector(-13, -4)]),
                       mask=HitboxMask.bullet,  # tell physics engine about object type
                       collision_mask=HitboxMask.enemy,  # tell physics engine which objects it can collide with
                       trigger_id=settings.COLLISION_TRIGGER_MG_BULLET
                       # ID to be used in custom collision handling function
                       ))