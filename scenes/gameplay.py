from kaa.engine import Scene

class GameplayScene(Scene):

    def __init__(self):
        super().__init__()

    def update(self, dt):

        for event in self.input.events():
            if event.is_quit():
                self.engine.quit()
