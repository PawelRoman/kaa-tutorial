import math
import settings
import registry
import random
from kaa.physics import CollisionPhase
from kaa.nodes import Node
from kaa.geometry import Alignment
from kaa.transitions import NodeSpriteTransition

class CollisionsController:

    def __init__(self, scene):
        self.scene = scene
        self.space = self.scene.space
        self.space.set_collision_handler(settings.COLLISION_TRIGGER_MG_BULLET, settings.COLLISION_TRIGGER_ENEMY,
                                         self.on_collision_mg_bullet_enemy)

        self.space.set_collision_handler(settings.COLLISION_TRIGGER_GRENADE_LAUNCHER_BULLET,
                                         settings.COLLISION_TRIGGER_ENEMY,
                                         self.on_collision_grenade_enemy)

    def on_collision_mg_bullet_enemy(self, arbiter, mg_bullet_pair, enemy_pair):
        print("Detected a collision between MG bullet object {} hitbox {} and Enemy object {} hitbox {}".format(
            mg_bullet_pair.body, mg_bullet_pair.hitbox, enemy_pair.body, enemy_pair.hitbox))

        if arbiter.phase == CollisionPhase.begin:
            enemy = enemy_pair.body
            enemy.hp -= 10
            # add the blood splatter animation to the scene
            self.scene.root.add_child(Node(z_index=900,
                                           transition=NodeSpriteTransition(
                                               registry.global_controllers.assets_controller.blood_splatter_frames,
                                               duration=140),
                                           position=enemy.position, rotation=mg_bullet_pair.body.rotation + math.pi,
                                           lifetime=140))
            # add a random bloodstain - make smaller ones more likely since it's a small arms hit :)
            self.scene.root.add_child(Node(z_index=1, sprite=random.choices(
                registry.global_controllers.assets_controller.bloodstain_imgs, weights=[5, 3, 1, 0.5])[0],
                                           position=enemy.position, rotation=mg_bullet_pair.body.rotation + math.pi,
                                           lifetime=random.randint(20000, 40000)))
            if enemy.hp <= 0:
                # show death animation
                self.scene.root.add_child(Node(z_index=1,
                                               transition=NodeSpriteTransition(random.choice(
                                                   registry.global_controllers.assets_controller.enemy_death_frames),
                                                   duration=450),
                                               position=enemy.position, rotation=enemy.rotation,
                                               origin_alignment=Alignment.right,
                                               lifetime=random.randint(10000, 20000)))
                # remove enemy node from the scene
                self.scene.enemies_controller.remove_enemy(enemy)
            else:
                enemy.stagger()

            mg_bullet_pair.body.delete()  # remove the bullet from the scene
            return 0

    def on_collision_grenade_enemy(self, arbiter, grenade_pair, enemy_pair):

        if arbiter.phase == CollisionPhase.begin:
            # show explosion animation
            self.scene.root.add_child(Node(transition=NodeSpriteTransition(
                registry.global_controllers.assets_controller.explosion_frames, duration=12*75),
                position=grenade_pair.body.position, z_index=1000, lifetime=12*75))
            # apply explosion effects to enemies (deal damage & push them back)
            self.scene.enemies_controller.apply_explosion_effects(grenade_pair.body.position)

            grenade_pair.body.delete()  # remove the grenade from the scene
            return 0