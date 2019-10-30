import settings
from kaa.input import Keycode
from common.enums import WeaponType
from objects.player import Player
from kaa.geometry import Vector


class PlayerController:

    def __init__(self, scene):
        self.scene = scene
        self.player = Player(position=Vector(settings.VIEWPORT_WIDTH/2, settings.VIEWPORT_HEIGHT/2))
        self.scene.root.add_child(self.player)

    def update(self, dt):
        if self.scene.input.is_pressed(Keycode.w):
            self.player.position += Vector(0, -3)
        if self.scene.input.is_pressed(Keycode.s):
            self.player.position += Vector(0, 3)
        if self.scene.input.is_pressed(Keycode.a):
            self.player.position += Vector(-3, 0)
        if self.scene.input.is_pressed(Keycode.d):
            self.player.position += Vector(3, 0)

        for event in self.scene.input.events():
            if event.is_pressing(Keycode.tab):
                self.player.cycle_weapons()
            if event.is_pressing(Keycode.num_1):
                self.player.change_weapon(WeaponType.MachineGun)
            if event.is_pressing(Keycode.num_2):
                self.player.change_weapon(WeaponType.GrenadeLauncher)
            if event.is_pressing(Keycode.num_3):
                self.player.change_weapon(WeaponType.ForceGun)

        mouse_pos = self.scene.input.get_mouse_position()
        player_rotation_vector = mouse_pos - self.player.position
        self.player.rotation_degrees = player_rotation_vector.to_angle_degrees()
