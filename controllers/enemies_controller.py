import random

from common.enums import EnemyMovementMode
from objects.enemy import Enemy
from kaa.geometry import Vector


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
                enemy.velocity += Vector.from_angle_degrees(enemy.rotation_degrees).normalize()*\
                                  (enemy.acceleration_per_second*dt/1000)


