from kaa.engine import Engine, Scene
from kaa.geometry import Vector
from kaa.sprites import Sprite
import os

# creating objects outside engine's 'with' context like this will cause your program crash:
loose_sprite = Sprite(os.path.join('assets', 'gfx', 'arrow.png'))


# everything else below is good!
class MyScene(Scene):

    def update(self, dt):
        for event in self.input.events():
            if event.is_quit():
                self.engine.quit()


with Engine(virtual_resolution=Vector(800, 600)) as engine:
    my_scene = MyScene()
    engine.run(my_scene)
