"""robo_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, Motion

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

keyboard.enable(timestep)



wave = Motion("../../motions/wave.motion")

def startMotion(motion):
    motion.play()


while robot.step(timestep) != -1:
    key = keyboard.getKey()
    
    if key == Keyboard.UP:
        startMotion(wave)

