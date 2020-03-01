import random
import registry
import math
from common.enums import EnemyMovementMode
from objects.enemy import Enemy
from kaa.geometry import Vector, Alignment
from kaa.nodes import Node
from kaa.transitions import NodeSpriteTransition

class EnemiesController:

    def __init__(self, scene):
        self.scene = scene
        self.enemies = []
        # add some initial enemies
        self.add_enemy(Enemy(position=Vector(200, 200), rotation_degrees=random.randint(0, 360)))
        self.add_enemy(Enemy(position=Vector(1500, 600), rotation_degrees=random.randint(0, 360)))
        self.add_enemy(Enemy(position=Vector(1000, 400), rotation_degrees=random.randint(0, 360)))
        self.add_enemy(Enemy(position=Vector(1075, 420), rotation_degrees=random.randint(0, 360)))
        self.add_enemy(Enemy(position=Vector(1150, 440), rotation_degrees=random.randint(0, 360)))

    def add_enemy(self, enemy):
        self.enemies.append(enemy)  # add to the internal list
        self.scene.space.add_child(enemy)  # add to the scene

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)  # remove from the internal list
        enemy.delete()  # remove from the scene
        # increment the frag counter
        self.scene.score_frag()

    def update(self, dt):
        player_pos = self.scene.player_controller.player.position

        for enemy in self.enemies:
            # handle enemy stagger time and stagger recovery
            if enemy.stagger_time_left > 0:
                enemy.stagger_time_left -= dt
                if enemy.stagger_time_left <= 0:
                    enemy.recover_from_stagger()

            # handle enemy movement
            if enemy.movement_mode == EnemyMovementMode.MoveToWaypoint:
                # rotate towards the current waypoint:
                enemy.rotation_degrees = (enemy.current_waypoint - enemy.position).to_angle_degrees()
                # # if we're less than 10 units from the waypoint, we randomize a new one!
                if (enemy.current_waypoint - enemy.position).length() <= 10:
                    enemy.randomize_new_waypoint()
            elif enemy.movement_mode == EnemyMovementMode.MoveToPlayer:
                # rotate towards the player:
                enemy.rotation_degrees = (player_pos - enemy.position).to_angle_degrees()
            else:
                raise Exception('Unknown enemy movement mode: {}'.format(enemy.movement_mode))

            # if enemy velocity is lower than max velocity, then increment velocity. Otherwise do nothing - the enemy
            # will be a freely moving object until the damping slows it down below max speed
            if enemy.velocity.length() < enemy.max_velocity:
                # increment the velocity
                enemy.velocity += Vector.from_angle_degrees(enemy.rotation_degrees).normalize() * \
                                  (enemy.acceleration_per_second * dt / 1000)

    def apply_explosion_effects(self, explosion_center, damage_at_center=100, blast_radius=200,
                                pushback_force_at_center=500, pushback_radius=300):
        # play explosion sound
        registry.global_controllers.assets_controller.explosion_sound.play()
        enemies_to_remove = []
        for enemy in self.enemies:
            # get the distance to the explosion
            distance_to_explosion = enemy.position.distance(explosion_center)

            # if within pushback radius...
            if distance_to_explosion<=pushback_radius:
                # calculate pushback value, the further from the center, the smaller it is
                pushback_force_val = pushback_force_at_center * (1 - (distance_to_explosion/pushback_radius))
                # apply the pushback force by resetting enemy velocity
                enemy.velocity = (enemy.position-explosion_center).normalize()*pushback_force_val

            # if within blast radius...
            if distance_to_explosion<=blast_radius:
                # calculate damage, the further from the center, the smaller it is
                damage = damage_at_center * (1 - (distance_to_explosion/blast_radius))
                # apply damage
                enemy.hp -= int(damage)
                # add the blood splatter animation over the enemy
                self.scene.root.add_child(Node(z_index=900,
                                               transition=NodeSpriteTransition(
                                                   registry.global_controllers.assets_controller.blood_splatter_frames,
                                                   duration=140),
                                               position=enemy.position, rotation=(enemy.position-explosion_center).to_angle() + math.pi,
                                               lifetime=140))

                if enemy.hp < 0:  # IZ DED!
                    # show the death animation (pick random sprite from few animations we have loaded from one png file)
                    self.scene.root.add_child(Node(z_index=1,
                                                   transition=NodeSpriteTransition(random.choice(
                                                       registry.global_controllers.assets_controller.enemy_death_frames),
                                                       duration=450),
                                                   position=enemy.position, rotation=enemy.rotation,
                                                   origin_alignment=Alignment.right,
                                                   lifetime=random.randint(10000,20000)))
                    # mark enemy for removal:
                    enemies_to_remove.append(enemy)

        # removed killed enemies
        for dead_enemy in enemies_to_remove:
            self.remove_enemy(dead_enemy)