import registry
import settings
import math
from kaa.engine import Scene
from kaa.input import Keycode, Mousecode
from kaa.nodes import Node
from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode
from kaa.transitions import *
from kaa.colors import Color

from scenes.gameplay import GameplayScene


class TitleScreenScene(Scene):

    def __init__(self):
        super().__init__()
        self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.title_screen_background_img,
                                 z_index=0, position=Vector(0,0), origin_alignment=Alignment.top_left))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH/2, 500), text="Click to start the game",
                                     z_index=1, origin_alignment=Alignment.center))
        self.exit_label = TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH/2, 550), text="Press ESC to exit",
                                     z_index=1, origin_alignment=Alignment.center)
        self.root.add_child(self.exit_label)
        self.transitions_fun_stuff()


    def start_new_game(self):
        registry.scenes.gameplay_scene = GameplayScene()
        self.engine.change_scene(registry.scenes.gameplay_scene)

    def transition_callback_function(self, node):
        registry.global_controllers.assets_controller.explosion_sound.play()

    def transitions_fun_stuff(self):
        move_transition = NodePositionTransition(Vector(-50, 200), duration=1000, advance_method=AttributeTransitionMethod.add)
        callback_transition = NodeTransitionCallback(self.transition_callback_function)
        rotate_transition = NodeRotationTransition(2*math.pi, duration=1000) # rotate 180 degrees (2*pi radians)
        wait_transition = NodeTransitionDelay(duration=500)
        scale_transition = NodeScaleTransition(Vector(2, 2), duration=1000) # enlarge twice
        color_transition = NodeColorTransition(Color(1, 0, 0, 1), duration=1000) # change color to red
        transition_sequence = NodeTransitionsSequence([move_transition, callback_transition,
                                                       rotate_transition, wait_transition,
                                                       scale_transition, color_transition])
        self.exit_label.transition = transition_sequence


    def update(self, dt):
        for event in self.input.events():
            if event.is_pressing(Keycode.escape):
                self.engine.quit()
            if event.is_quit():
                self.engine.quit()
            if event.is_pressing(Mousecode.left):
                self.start_new_game()