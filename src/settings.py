class ScreenSettings():

    def __init__(self, width = 800, height = 600):
        self.width = width
        self.height = height
        self.bg_color = (200, 200, 200)

class ShipSettings():

    def __init__(self, speed_factor = 0.5):
        self.speed_factor = speed_factor

class BulletSettings():

    def __init__(self, speed_factor = 1, width = 3, height = 15, color = (30, 30, 30) ):
        self.speed_factor = speed_factor
        self.width = width
        self.height = height
        self.color = color
        self.bullets_allowed = 3

class GameSettings():

    def __init__(self):
        self.screenSettings = ScreenSettings()
        self.shipSettings = ShipSettings()
        self.bulletSettings = BulletSettings()

