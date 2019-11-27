from kaa.engine import Engine
from kaa.geometry import Vector
import settings
import registry
from controllers.assets_controller import AssetsController
from scenes.gameplay import GameplayScene
from scenes.pause import PauseScene
from scenes.title_screen import TitleScreenScene

with Engine(virtual_resolution=Vector(settings.VIEWPORT_WIDTH, settings.VIEWPORT_HEIGHT)) as engine:
    # initialize global controllers and remember them in the registry
    registry.global_controllers.assets_controller = AssetsController()
    # play music
    registry.global_controllers.assets_controller.music_track_1.play()
    # set window to fullscreen mode
    engine.window.fullscreen = True
    # initialize scenes and remember them in the registry
    registry.scenes.gameplay_scene = GameplayScene()
    registry.scenes.title_screen_scene = TitleScreenScene()
    registry.scenes.pause_scene = PauseScene()
    engine.run(registry.scenes.title_screen_scene)
