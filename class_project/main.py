from ev3Brick import EV3Brick
from motor import Motor
from port import Port
from sensor import Sensor
from driveBase import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

light_sensor = Sensor(Port.S1)

# Initialize the drive base.
drivebase = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

drivebase.straight(1000)
drivebase.straight(400)
drivebase.straight(300)
drivebase.straight(-500)
drivebase.straight(1400)

print(drivebase.position)

drivebase.turn(730)


times = drivebase.deg / 360
result = drivebase.deg - (times * 360)

print(result)
