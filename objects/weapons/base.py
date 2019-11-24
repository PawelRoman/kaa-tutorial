from kaa.nodes import Node
from kaa.geometry import Vector


class WeaponBase(Node):

    def __init__(self, *args, **kwargs):
        super().__init__(z_index=20, *args, **kwargs)
        self.cooldown_time_remaining = 0

    def shoot_bullet(self):
        raise NotImplementedError  # must be implemented in the derived class

    def get_cooldown_time(self):
        raise NotImplementedError  # must be implemented in the derived class

    def get_initial_bullet_position(self):
        player_pos = self.parent.position
        player_rotation = self.parent.rotation_degrees
        weapon_length = 35  # the bullet won't originate in the center of the player position but 30 pixels from it
        result = player_pos + Vector.from_angle_degrees(player_rotation).normalize()*weapon_length
        return result
