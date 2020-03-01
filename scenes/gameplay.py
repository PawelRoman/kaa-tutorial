from kaa.engine import Scene

from controllers.collisions_controller import CollisionsController
from controllers.player_controller import PlayerController
from controllers.enemies_controller import EnemiesController
from kaa.nodes import Node
from kaa.input import Keycode
from kaa.physics import SpaceNode
import registry
import settings
from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode
from kaa.colors import Color

class GameplayScene(Scene):

    def __init__(self):
        super().__init__()
        self.frag_count = 0
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_1,
                                     origin_alignment=Alignment.left, position=Vector(10, 20), font_size=40, z_index=1,
                                     text="WASD to move, mouse to rotate, left mouse button to shoot"))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_1,
                                     origin_alignment=Alignment.left, position=Vector(10, 45), font_size=40, z_index=1,
                                     text="1, 2, 3 - change weapons. SPACE - spawn enemy"))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2,
                                     origin_alignment=Alignment.right, position=Vector(1910, 20), font_size=30,
                                     z_index=1,
                                     color=Color(1, 0, 0, 1), text="Press Q to quit game"))
        self.frag_count_label = TextNode(font=registry.global_controllers.assets_controller.font_1,
                                         origin_alignment=Alignment.left, position=Vector(10, 70), font_size=40,
                                         z_index=1,
                                         color=Color(1, 1, 0, 1), text="")
        self.root.add_child(self.frag_count_label)

        self.space = SpaceNode(damping=0.3)
        self.root.add_child(self.space)
        self.player_controller = PlayerController(self)
        self.enemies_controller = EnemiesController(self)
        self.collisions_controller = CollisionsController(self)
        self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.background_img,
                                 position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2),
                                 z_index=0))
    def update(self, dt):
        self.player_controller.update(dt)
        self.enemies_controller.update(dt)

        for event in self.input.events():
            if event.keyboard_key:  # check if the event is a keyboard key related event
                if event.keyboard_key.is_key_down:  # check if the event is "key down event"
                    # check which key was pressed down:
                    if event.keyboard_key.key == Keycode.q:
                        self.engine.quit()
                    if event.keyboard_key.key == Keycode.escape:
                        self.engine.change_scene(registry.scenes.pause_scene)

        if self.input.keyboard.is_pressed(Keycode.left):
            self.camera.position -= Vector(-0.1 * dt, 0)
        if self.input.keyboard.is_pressed(Keycode.right):
            self.camera.position -= Vector(0.1 * dt, 0)
        if self.input.keyboard.is_pressed(Keycode.up):
            self.camera.position -= Vector(0, -0.1 * dt)
        if self.input.keyboard.is_pressed(Keycode.down):
            self.camera.position -= Vector(0, 0.1 * dt)

        if self.input.keyboard.is_pressed(Keycode.pageup):
            self.camera.scale -= Vector(0.001*dt, 0.001*dt)
        if self.input.keyboard.is_pressed(Keycode.pagedown):
            self.camera.scale += Vector(0.001*dt, 0.001*dt)

        if self.input.keyboard.is_pressed(Keycode.home):
            self.camera.rotation_degrees += 0.03 * dt
        if self.input.keyboard.is_pressed(Keycode.end):
            self.camera.rotation_degrees -= 0.03 * dt

    def score_frag(self):
        # function for tracking frag count
        self.frag_count += 1
        self.frag_count_label.text = f"Frag Count: {self.frag_count}"