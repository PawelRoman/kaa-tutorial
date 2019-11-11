from kaa.physics import BodyNodeType, BodyNode, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import HitboxMask
import registry
import settings


class Enemy(BodyNode):

    def __init__(self, position, hp=100, *args, **kwargs):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic, mass=1,
                         z_index=10, sprite=registry.global_controllers.assets_controller.enemy_img, position=position,
                         *args, **kwargs)
        # create a hitbox and add it as a child node to the Enemy
        self.add_child(HitboxNode(
            shape=Polygon([Vector(-8, -19), Vector(8, -19), Vector(8, 19), Vector(-8, 19), Vector(-8, -19)]),
            mask=HitboxMask.enemy,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_ENEMY,
        ))
        # custom properties
        self.hp = hp
        self.stagger_time_left = 0

    def stagger(self):
        # use "stagger" frame
        self.sprite.frame_current = 1
        # track time for staying in the staggered state
        self.stagger_time_left = 150

    def recover_from_stagger(self):
        self.sprite.frame_current = 0
        self.stagger_time_left = 0

