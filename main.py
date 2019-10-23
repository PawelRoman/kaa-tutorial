from kaa.engine import Engine, Scene
from kaa.geometry import Vector, Alignment
from kaa.sprites import Sprite
from kaa.nodes import Node
import os


class MyScene(Scene):

    def __init__(self):
        super().__init__()
        self.arrow_sprite = Sprite(os.path.join('assets', 'gfx', 'arrow.png'))
        self.arrow1 = Node(sprite=self.arrow_sprite, position=Vector(200, 200))
        self.arrow2 = Node(sprite=self.arrow_sprite, position=Vector(400, 300))
        self.arrow3 = Node(sprite=self.arrow_sprite, position=Vector(600, 500))
        self.root.add_child(self.arrow1)
        self.root.add_child(self.arrow2)
        self.root.add_child(self.arrow3)
        self.arrow1.position = Vector(360, 285)
        self.arrow1.z_index = 1  # note: default z_index is 0
        self.arrow1.rotation_degrees = 45  # note: default rotation_degrees is 0
        self.arrow1.scale = Vector(0.5, 1)  # note: default is Vector(1,1)
        # create pixel marker sprite
        self.pixel_marker_sprite = Sprite(os.path.join('assets', 'gfx', 'pixel-marker.png'))
        # create pixel_marker 1 in the same spot as arrow2 (but with bigger z-index so we can see it)
        self.pixel_marker1 = Node(sprite=self.pixel_marker_sprite, position=Vector(400, 300), z_index=100)
        # create pixel_marker 2 in the same spot as arrow3
        self.pixel_marker2 = Node(sprite=self.pixel_marker_sprite, position=Vector(600, 500), z_index=100)
        # add pixel markers to the scene
        self.root.add_child(self.pixel_marker1)
        self.root.add_child(self.pixel_marker2)
        self.arrow3.origin_alignment = Alignment.right  # default is Alignment.center
        self.green_arrow_sprite = Sprite(os.path.join('assets', 'gfx', 'arrow-green.png'))
        self.child_arrow1 = Node(sprite=self.green_arrow_sprite, position=Vector(0, 0), rotation_degrees=90, z_index=1)
        self.arrow3.add_child(self.child_arrow1)
        self.explosion_sprite_looped = Sprite(os.path.join('assets', 'gfx', 'explosion.png'), frame_count=75,
                                              frame_dimensions=Vector(100, 100), animation_frame_duration=25,
                                              animation_loop=True)
        self.explosion = Node(sprite=self.explosion_sprite_looped, position=Vector(600, 150))
        self.root.add_child(self.explosion)

        self.explosion_sprite_long = Sprite(os.path.join('assets', 'gfx', 'explosion.png'), frame_count=75,
                                            frame_dimensions=Vector(100, 100), animation_frame_duration=100)
        self.explosion2 = Node(sprite=self.explosion_sprite_long, position=Vector(100, 400))
        self.explosion3 = Node(sprite=self.explosion_sprite_long, position=Vector(200, 500))
        self.root.add_child(self.explosion2)
        self.root.add_child(self.explosion3)

        self.explosion_sprite_cropped = Sprite(os.path.join('assets', 'gfx', 'explosion.png'), frame_count=5,
                                               frame_dimensions=Vector(100, 100), animation_frame_duration=1000).crop(
            Vector(0, 300), Vector(500, 100))
        self.explosion_cropped = Node(sprite=self.explosion_sprite_cropped, position=Vector(300, 100), lifetime=5000)
        self.root.add_child(self.explosion_cropped)

    def update(self, dt):
        for event in self.input.events():
            if event.is_quit():
                self.engine.quit()
        self.arrow2.rotation_degrees += 1  # rotating 1 degree PER FRAME (not the best design)
        self.arrow3.rotation_degrees += 90 * dt / 1000  # rotating 90 degrees PER SECOND (good design!)


with Engine(virtual_resolution=Vector(800, 600)) as engine:
    # initialize and run the scene
    my_scene = MyScene()
    engine.run(my_scene)
