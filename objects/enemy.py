from kaa.physics import BodyNodeType, BodyNode, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import HitboxMask, EnemyMovementMode
import registry
import settings
import random


class Enemy(BodyNode):

    def __init__(self, position, hp=100, *args, **kwargs):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic,
                         mass=1,
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
        # 75% enemies will move towards player and 25% will move randomly
        if random.randint(0, 100) < 75:
            self.movement_mode = EnemyMovementMode.MoveToPlayer
        else:
            self.movement_mode = EnemyMovementMode.MoveToWaypoint
        self.current_waypoint = None  # for those which move to a waypoint, we'll keep its corrdinates here
        self.randomize_new_waypoint()  # and randomize new waypoint

        self.acceleration_per_second = 300  # how fast will enemy accelerate
        self.max_velocity = random.randint(75, 125)  # we'll make enemy stop accelerating if velocity is above this value


    def stagger(self):
        # use "stagger" frame
        self.sprite.frame_current = 1
        # track time for staying in the staggered state
        self.stagger_time_left = 150

    def recover_from_stagger(self):
        self.sprite.frame_current = 0
        self.stagger_time_left = 0

    def randomize_new_waypoint(self):
        self.current_waypoint = Vector(random.randint(50, settings.VIEWPORT_WIDTH-50),
                                       random.randint(50, settings.VIEWPORT_HEIGHT-50))