from kaa.nodes import Node


class WeaponBase(Node):

    def __init__(self, *args, **kwargs):
        super().__init__(z_index=20, *args, **kwargs)
