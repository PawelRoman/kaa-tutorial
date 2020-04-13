from kaa.engine import Engine
from kaa.geometry import Vector
import settings
from scenes.gameplay import GameplayScene
from scenes.pause import PauseScene
from scenes.title_screen import TitleScreenScene
import registry
from controllers.assets_controller import AssetsController

if __name__ == "__main__":

    with Engine(virtual_resolution=Vector(settings.VIEWPORT_WIDTH, settings.VIEWPORT_HEIGHT)) as engine:
        # initialize global controllers and keep them in the registry
        registry.global_controllers.assets_controller = AssetsController()
        # play music
        registry.global_controllers.assets_controller.music_track_1.play()
        # set window to fullscreen mode
        engine.window.fullscreen = True
        # initialize and run the scene
        registry.scenes.gameplay_scene = GameplayScene()
        registry.scenes.title_screen_scene = TitleScreenScene()
        registry.scenes.pause_scene = PauseScene()
        engine.run(registry.scenes.title_screen_scene)