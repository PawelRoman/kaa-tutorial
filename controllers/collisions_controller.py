import math
import settings
import registry
from kaa.physics import CollisionPhase
from kaa.nodes import Node
from kaa.geometry import Alignment

class CollisionsController:

    def __init__(self, scene):
        self.scene = scene
        self.space = self.scene.space
        self.space.set_collision_handler(settings.COLLISION_TRIGGER_MG_BULLET, settings.COLLISION_TRIGGER_ENEMY,
                                         self.on_collision_mg_bullet_enemy)

    def on_collision_mg_bullet_enemy(self, arbiter, mg_bullet_pair, enemy_pair):
        print("Detected a collision between MG bullet object {} hitbox {} and Enemy object {} hitbox {}".format(
            mg_bullet_pair.body, mg_bullet_pair.hitbox, enemy_pair.body, enemy_pair.hitbox))

        if arbiter.phase == CollisionPhase.begin:
            enemy = enemy_pair.body
            enemy.hp -= 10
            # add the blood splatter animation to the scene
            self.scene.root.add_child(Node(z_index=900,
                                           sprite=registry.global_controllers.assets_controller.blood_splatter_img,
                                           position=enemy.position, rotation=mg_bullet_pair.body.rotation + math.pi,
                                           lifetime=3000))
            if enemy.hp<=0:
                # show death animation
                self.scene.root.add_child(Node(z_index=1,
                                               sprite=registry.global_controllers.assets_controller.enemy_death_img,
                                               position=enemy.position, rotation=enemy.rotation,
                                               origin_alignment = Alignment.right,
                                               lifetime=10000))
                # remove enemy node from the scene
                self.scene.enemies_controller.remove_enemy(enemy)
            else:
                enemy.stagger()

            mg_bullet_pair.body.delete()  # remove the bullet from the scene
