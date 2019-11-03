from kaa.nodes import Node
import registry


class GrenadeLauncherBullet(Node):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.grenade_launcher_bullet_img, *args, **kwargs)
