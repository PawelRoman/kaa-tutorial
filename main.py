from kaa.engine import Engine
from kaa.geometry import Vector
import settings
import registry
from controllers.assets_controller import AssetsController
from scenes.gameplay import GameplayScene

with Engine(virtual_resolution=Vector(settings.VIEWPORT_WIDTH, settings.VIEWPORT_HEIGHT)) as engine:
    # initialize global controllers and remember them in the registry
    registry.global_controllers.assets_controller = AssetsController()
    # set window to fullscreen mode
    engine.window.fullscreen = True
    # initialize scenes and remember them in the registry
    registry.scenes.gameplay_scene = GameplayScene()
    engine.run(registry.scenes.gameplay_scene)
