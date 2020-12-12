class DriveBase:

    left_motor = 0
    right_motor = 0
    countMotors = 0
    wheel_diameter=55.5
    axle_track=104
    position = 0
    deg = 0

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        if left_motor:
            self.countMotors = self.countMotors + 1
        if right_motor:
            self.countMotors = self.countMotors + 1
        
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        print("DRIVEBASE READY")
    
    def straight(self, mm):
        self.position = self.position + mm
    
    def turn(self, deg):
        self.deg = self.deg + deg
        

