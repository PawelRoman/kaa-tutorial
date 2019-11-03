import enum

class WeaponType(enum.Enum):
    MachineGun = 1
    GrenadeLauncher = 2
    ForceGun = 3


class HitboxMask(enum.IntFlag):
    player = enum.auto()
    enemy = enum.auto()
    bullet = enum.auto()

    all = player | enemy | bullet
