import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

gripper = 0

# pulse_width_range sets the min and max range of the servo: where the servo actually goes to
# these values will determine where the servo 0 degrees starts
kit.servo[gripper].set_pulse_width_range(1000, 2000)

# note that the angle is wrt to actuation_range, not the absolute angle!!!
kit.servo[gripper].actuation_range = 90

kit.servo[gripper].angle = 0
time.sleep(1.0)
print("Open gripper: ", kit.servo[gripper].angle)

kit.servo[gripper].angle = 65
time.sleep(1.0)
print("Close gripper: ", kit.servo[gripper].angle)


kit.servo[gripper].angle = 0
time.sleep(1.0)
print("Open gripper: ", kit.servo[gripper].angle)

kit.servo[gripper].angle = 60
time.sleep(1.0)
print("Grasp rubber: ", kit.servo[gripper].angle)
