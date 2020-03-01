import registry
import settings
from kaa.engine import Scene
from kaa.input import Keycode, MouseButton
from kaa.nodes import Node
from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode
from kaa.transitions import *
import math
from kaa.colors import Color

from scenes.gameplay import GameplayScene


class TitleScreenScene(Scene):

    def __init__(self):
        super().__init__()
        self.root.add_child(Node(sprite=registry.global_controllers.assets_controller.title_screen_background_img,
                                 z_index=0, position=Vector(0, 0), origin_alignment=Alignment.top_left))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH / 2, 500), text="Click to start the game",
                                     z_index=1, origin_alignment=Alignment.center))
        self.exit_label = TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                   position=Vector(settings.VIEWPORT_WIDTH / 2, 550), text="Press ESC to exit",
                                   z_index=1, origin_alignment=Alignment.center)
        self.root.add_child(self.exit_label)
        self.transitions_fun_stuff()

    def start_new_game(self):
        registry.scenes.gameplay_scene = GameplayScene()
        self.engine.change_scene(registry.scenes.gameplay_scene)

    def update(self, dt):
        for event in self.input.events():

            if event.keyboard_key:
                if event.keyboard_key.is_key_down and event.keyboard_key.key == Keycode.escape:
                    self.engine.quit()

            if event.mouse_button:
                #print('mouse button event {}'.format(event.mouse_button.button))
                if event.mouse_button.is_button_down and event.mouse_button.button() == MouseButton.left:
                    self.engine.change_scene(registry.scenes.gameplay_scene)
            if event.mouse_button and event.mouse_button.is_button_down and event.mouse_button.button() == MouseButton.left:
                self.start_new_game()

    def transition_callback_function(self, node):
        # play explosion sound
        registry.global_controllers.assets_controller.explosion_sound.play()

    def transitions_fun_stuff(self):
        rotate_transition = NodeRotationTransition(2*math.pi, duration=1000) # rotate 180 degrees (2*pi radians)
        scale_transition = NodeScaleTransition(Vector(2, 2), duration=1000) # enlarge twice
        color_transition = NodeColorTransition(Color(1, 0, 0, 1), duration=1000) # change color to red

        move_transition1 = NodePositionTransition(Vector(-200, 0), duration=1000,
                                           advance_method=AttributeTransitionMethod.add)
        move_transition2 = NodePositionTransition(Vector(200, 200), duration=1000,
                                           advance_method=AttributeTransitionMethod.add)
        move_transition3 = NodePositionTransition(Vector(200, -200), duration=1000,
                                           advance_method=AttributeTransitionMethod.add)
        move_transition4 = NodePositionTransition(Vector(-200, 0), duration=1000,
                                           advance_method=AttributeTransitionMethod.add)

        move_sequence = NodeTransitionsSequence([move_transition1, move_transition2, move_transition3, move_transition4], loops=0)
        paralel_sequence = NodeTransitionsParallel([rotate_transition, scale_transition, color_transition], back_and_forth=True, loops=0)

        # run both the movement sequence and rotate+scale+color sequence in paralel
        self.exit_label.transition = NodeTransitionsParallel([
            move_sequence, paralel_sequence])

