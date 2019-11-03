from kaa.nodes import Node
import registry


class MachineGunBullet(Node):

    def __init__(self, *args, **kwargs):
        super().__init__(sprite=registry.global_controllers.assets_controller.machine_gun_bullet_img, *args, **kwargs)
