class ScreenSettings():

    def __init__(self, width=800, height=600,
            caption="SimpleGameWrittenInPygame"):
        self.width = width
        self.height = height
        self.bg_color = (100, 200, 200)
        self.caption = caption

class ShipSettings():

    def __init__(self, speed_factor=0.3, image_resolution=(45, 60), 
            image_path="./images/ship.bmp"):
        self.speed_factor = speed_factor
        self.image_resolution = image_resolution
        self.image_path = image_path

class BulletSettings():

    def __init__(self, speed_factor=1, image_resolution=(30, 30), 
            image_path="./images/bullet.bmp"):
        self.speed_factor = speed_factor
        self.image_resolution = image_resolution
        self.image_path = image_path

class BulletsSettings():
    def __init__(self, bullet_settings=BulletSettings(), max_amount=3):
        self.bullet_settings = bullet_settings

        #the maximum number of bullets on the screen at the same time
        self.max_amount = max_amount

class DVDLogoSettings():
    def __init__(self, speed_factor=0.3, image_resolution=(80, 80), 
            image_path="./images/dvd_logo.bmp"):
        self.speed_factor = speed_factor
        self.image_resolution = image_resolution
        self.image_path = image_path

class DVDLogosSettings():
    def __init__(self, dvd_logo_settings=DVDLogoSettings()):
        self.dvd_logo_settings = dvd_logo_settings

class CollisionDetectorSettings():
    def __init__(self):
        pass

class GameSettings():
    def __init__(self):
        self.screen_settings = ScreenSettings()
        self.ship_settings = ShipSettings()
        self.bullets_settings = BulletsSettings()
        self.dvd_logos_settings = DVDLogosSettings()
        self.collison_detector_settings = CollisionDetectorSettings()
