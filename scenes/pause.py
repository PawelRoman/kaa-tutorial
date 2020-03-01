import registry
import settings
from kaa.engine import Scene
from kaa.input import Keycode
from kaa.geometry import Vector, Alignment
from kaa.fonts import TextNode


class PauseScene(Scene):

    def __init__(self):
        super().__init__()
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=40,
                                     position=Vector(settings.VIEWPORT_WIDTH / 2, 300), text="GAME PAUSED",
                                     z_index=1, origin_alignment=Alignment.center))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH / 2, 550), text="Press ESC to resume",
                                     z_index=1, origin_alignment=Alignment.center))
        self.root.add_child(TextNode(font=registry.global_controllers.assets_controller.font_2, font_size=30,
                                     position=Vector(settings.VIEWPORT_WIDTH / 2, 650), text="Press q to abort",
                                     z_index=1, origin_alignment=Alignment.center))

    def update(self, dt):
        for event in self.input.events():
            if event.keyboard_key and event.keyboard_key.is_key_down:
                if event.keyboard_key.key == Keycode.escape:
                    self.engine.change_scene(registry.scenes.gameplay_scene)
                if event.keyboard_key.key == Keycode.q:
                    self.engine.change_scene(registry.scenes.title_screen_scene)