class ScreenSettings():

    def __init__(self, width=800, height=600,
            caption="SimpleGameWrittenInPygame"):
        self.width = width
        self.height = height
        self.bg_color = (100, 200, 200)
        self.caption = caption

class ShipSettings():

    def __init__(self, speed_factor=0.3, image_resolution=(45, 60), 
            image_path="../images/ship.bmp"):
        self.speed_factor = speed_factor
        self.image_resolution = image_resolution
        self.image_path = image_path

class BulletSettings():

    def __init__(self, speed_factor=1, image_resolution=(30, 30), 
            image_path="../images/bullet.bmp"):
        self.speed_factor = speed_factor
        self.image_resolution = image_resolution
        self.image_path = image_path

class GameSettings():

    def __init__(self):
        self.screen_settings = ScreenSettings()
        self.ship_settings = ShipSettings()
        self.bullet_settings = BulletSettings()

