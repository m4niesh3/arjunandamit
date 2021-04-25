class Settings :
    """a class to store all setiings for alien invasion """

    def __init__(self) :
        """initialize the games settings"""
        #screen settings
        self.bullet_speed=1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=5
        self.ship_speed=1.5
        self.screen_width=1200
        self.screen_height=750
        self.bg_color=(240,230,140)
        #amit settings
        self.amit_speed=0.5
        self.fleet_drop_speed=10
        #fleet direction of 1 represent right; -1 represents left
        self.fleet_direction= 1


