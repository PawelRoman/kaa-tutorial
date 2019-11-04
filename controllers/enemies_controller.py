import random

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
        pass
