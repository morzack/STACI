from wpilib.command import CommandGroup

from commands import driveForwards, shootIntake, turnRobot

import robotmap

class PassAutoLineShoot(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.addSequential(driveForwards.DriveForward(robot, 170-robotmap.robotDiameter))
        self.addSequential(turnRobot.TurnRobot(robot, -20))
        self.addSequential(shootIntake.ShootIntake(robot, 2))
        self.addSequential(shootIntake.ShootIntake(robot, 1))