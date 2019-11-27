import registry
import settings
from kaa.engine import Scene
from kaa.input import Keycode
from kaa.physics import SpaceNode
from kaa.nodes import Node
from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode
from kaa.colors import Color

from controllers.collisions_controller import CollisionsController
from controllers.enemies_controller import EnemiesController
from controllers.player_controller import PlayerController


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
                            origin_alignment=Alignment.right, position=Vector(1910, 20), font_size=30, z_index=1,
                            color=Color(1, 0, 0, 1), text="Press Q to quit game"))
        self.frag_count_label = TextNode(font=registry.global_controllers.assets_controller.font_1,
                            origin_alignment=Alignment.left, position=Vector(10, 70), font_size=40, z_index=1,
                            color=Color(1, 1, 0, 1), text="Frag count: 0")
        self.root.add_child(self.frag_count_label)

        self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.background_img,
                                 position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2),
                                 z_index=0))
        self.space = SpaceNode(damping=0.3)
        self.root.add_child(self.space)
        self.player_controller = PlayerController(self)
        self.enemies_controller = EnemiesController(self)
        self.collisions_controller = CollisionsController(self)

    def score_frag(self):
        self.frag_count += 1
        self.frag_count_label.text = f"Frag Count: {self.frag_count}"

    def update(self, dt):
        self.player_controller.update(dt)
        self.enemies_controller.update(dt)

        for event in self.input.events():
            if event.is_pressing(Keycode.q):
                self.engine.quit()
            if event.is_quit():
                self.engine.quit()
            if event.is_pressing(Keycode.escape):
                self.engine.change_scene(registry.scenes.pause_scene)
