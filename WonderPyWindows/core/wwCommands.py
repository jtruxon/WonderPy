from WonderPyWindows.core.wwConstants import WWRobotConstants
from WonderPyWindows.components.wwCommandEyering import WWCommandEyering
from WonderPyWindows.components.wwCommandPing import WWCommandPing
from WonderPyWindows.components.wwCommandBody import WWCommandBody
from WonderPyWindows.components.wwCommandRGB import WWCommandRGB
from WonderPyWindows.components.wwCommandMonoLED import WWCommandMonoLED
from WonderPyWindows.components.wwCommandMedia import WWCommandMedia
from WonderPyWindows.components.wwCommandAccessory import WWCommandAccessory
from WonderPyWindows.components.wwCommandHead import WWCommandHead

_rc  = WWRobotConstants.RobotComponent
_rcv = WWRobotConstants.RobotComponentValues
_rp  = WWRobotConstants.RobotProperties


class WWCommands(object):

    def __init__(self, robot):
        self._robot = robot
        self.eyering    = WWCommandEyering  (robot)
        self.head       = WWCommandHead     (robot)
        self.media      = WWCommandMedia    (robot)
        self.monoLED    = WWCommandMonoLED  (robot)
        self.ping       = WWCommandPing     (robot)
        self.body       = WWCommandBody     (robot)
        self.RGB        = WWCommandRGB      (robot)
        self.accessory  = WWCommandAccessory(robot)
