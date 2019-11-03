from kaa.nodes import Node
import registry


class ForceGunBullet(Node):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.force_gun_bullet_img, *args, **kwargs)
