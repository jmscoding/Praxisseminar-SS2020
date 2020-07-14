"""
IN BEARBEITUNG:
- physischer Prozess im End Effekt nur starten und beenden des Fliessbandes und Bestimmen der Geschwindigkeit des Motors


Fliessband physical process

"""


from minicps.devices import Tank

#from utils import MOTOR_VEL
from utils import STATE, MOTOR_VEL, Praxisseminar_test_logger

import sys
import time


# Praxisseminar TAGS
# Beispiel: MV101 = ('MV101', 1)
MOTOR = ('MOTOR', 1)
SENSOR = ('SENSOR', 1)
# Praxisseminar TAGS


# Doch Klasse Tank verwendet da eigene Klasse nicht in Python Pfad hinterlegt ist
class ConveyorBelt(Tank):

    def pre_loop(self, sleep=0.1):

        # Praxisseminar STATE INIT(

        # Standardmaessig ist der Motor des Foerderbandes an
        get_m11 = self.get(MOTOR)
        Praxisseminar_test_logger.info('Motor: ' + str(get_m11))

        # Praxisseminar STATE INIT)

    def main_loop(self, sleep=0.1):

        count = 0
        while True:

            # ueberpruefe ob Motor an ist
            # wenn ja dann setze standarmaessig Anfangsgeschwindigkeit

            motor = self.get(MOTOR)
            Praxisseminar_test_logger.info('Motor: ' + str(motor))

            if int(motor) == 1:

                new_velocity = self.get(SENSOR)
                Praxisseminar_test_logger.info('Sensor: ' + str(new_velocity))
                if new_velocity == '0.0':
                    new_velocity = MOTOR_VEL['STD']
                    self.set(SENSOR, new_velocity)
                    Praxisseminar_test_logger.info('Sensordaten wurden veraendert: ' + str(new_velocity))
                else:
                    self.set(SENSOR, new_velocity)
                    Praxisseminar_test_logger.info('Sensordaten wurden veraendert: ' + str(new_velocity))

            # DEBUG 'Standarmaessige Motorgeschwindigkeit
            else:
                self.set(SENSOR, MOTOR_VEL['MIN'])
                Praxisseminar_test_logger.info('Sensordaten wurden veraendert: ' + str(MOTOR_VEL['MIN']))

            time.sleep(sleep)
            count += 1


if __name__ == '__main__':
# section, level, protocol???
    cb = ConveyorBelt(
        name='cb',
        state=STATE,
        protocol=None,
        section=None,
        level=None
    )
