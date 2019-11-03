from kaa.engine import Scene
from kaa.input import Keycode
from kaa.physics import SpaceNode

from controllers.player_controller import PlayerController


class GameplayScene(Scene):

    def __init__(self):
        super().__init__()
        self.space = SpaceNode()
        self.root.add_child(self.space)
        self.player_controller = PlayerController(self)


    def update(self, dt):
        self.player_controller.update(dt)

        for event in self.input.events():
            if event.is_pressing(Keycode.q):
                self.engine.quit()
            if event.is_quit():
                self.engine.quit()
