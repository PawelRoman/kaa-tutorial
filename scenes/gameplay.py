from kaa.engine import Scene

from controllers.player_controller import PlayerController


class GameplayScene(Scene):

    def __init__(self):
        super().__init__()
        self.player_controller = PlayerController(self)

    def update(self, dt):

        for event in self.input.events():
            if event.is_quit():
                self.engine.quit()
