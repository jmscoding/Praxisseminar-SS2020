"""
IN BEARBEITUNG:
- physischer Prozess im End Effekt nur starten und beenden des Fliessbandes und Bestimmen der Geschwindigkeit des Motors


Fliessband physical process

"""


from minicps.devices import Tank

#from utils import MOTOR_VEL
from utils import STATE

import sys
import time


# Praxisseminar TAGS
# Beispiel: MV101 = ('MV101', 1)
MOTOR = ('MOTOR', 1)
SENSOR = ('SENSOR', 1)
# Praxisseminar TAGS


# TODO:
class ConveyorBelt(Tank):

    def pre_loop(self, sleep=0.1):

        # Praxisseminar STATE INIT(

        # Standardmaessig ist der Motor des Foerderbandes an
        self.set(MOTOR, 0)

        # Praxisseminar STATE INIT)

    def main_loop(self, sleep=0.1):

        count = 0
        while(count == 1000):

            # ueberpruefe ob Motor an ist
            # wenn ja dann setze standarmaessig Anfangsgeschwindigkeit

            motor = self.get(MOTOR)

            if int(motor) == 1:

                new_velocity = self.get(SENSOR)
                self.set(SENSOR, new_velocity)


            # DEBUG 'Standarmaessige Motorgeschwindigkeit
            else:
                self.set(SENSOR, 0.0)


            time.sleep(sleep)
            count += 1



if __name__ == '__main__':

    cb = ConveyorBelt(
        name='cb',
        state=STATE,
        protocol=None,
        section=None,
        level=None
    )
