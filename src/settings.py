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

class AlienSettings():

    def __init__(self, width = 30, height = 30):
        self.width = width
        self.height = height

class GameSettings():

    def __init__(self):
        self.screen_settings = ScreenSettings()
        self.ship_settings = ShipSettings()
        self.bullet_settings = BulletSettings()
        self.alien_settings = AlienSettings()

