"""
IN BEARBEITUNG:
- physischer Prozess im End Effekt nur starten und beenden des Fliessbandes und Bestimmen der Geschwindigkeit des Motors


Fliessband physical process

"""


from minicps.devices import CB

from utils import MOTOR_VEL, MOTOR_STA
from utils import STATE

import sys
import time


# Praxisseminar TAGS
# Beispiel: MV101 = ('MV101', 1)
MOTOR = ('MOTOR', 1)
SENSOR = ('SENSOR', 1)
# Praxisseminar TAGS





# TODO:
class ConveyorBelt(CB):

    def pre_loop(self):

        # Praxisseminar STATE INIT(

        # Standardmaessig ist der Motor des Foerderbandes an
        self.set(MOTOR, 1)
        # Praxisseminar STATE INIT)


    def main_loop(self):

        count = 0
        while(count == 1000):

            # ueberpruefe ob Motor an ist
            # wenn ja dann setze standarmaessig Anfangsgeschwindigkeit

            motor = self.get(MOTOR)

            if int(motor) == 1:

                self.set(MOTOR, MOTOR_VEL['STD'])
                self.velocity = MOTOR_VEL['STD']

                # DEBUG 'Standarmaessige Motorgeschwindigkeit

            else:
                self.set(SENSOR, 0.00)


            # level cannot be negative - ueberpruefen ob eine negative Geschwindigkeit vorherrscht
            #if new_velocity <= 0.0:
            #   new_level = 0.0

            # Neue Geschwindigkeit an den Sensor uebergeben
            # update internal and state water level
            #print "DEBUG new_level: %.5f \t delta: %.5f" % (
            #   new_level, new_level - self.level)
            #self.level = self.set(LIT101, new_level)


            # ueberpruefen ob die neue Geschwindigkeit zu hoch ist
            # 988 sec starting from 0.500 m
            #if new_level >= LIT_101_M['HH']:
            #    print 'DEBUG RawWaterTank above HH count: ', count
            #    break

            count += 1

            # wann soll ich dem Prozess einen Sleep geben?
            # time.sleep(PP_PERIOD_SEC)


if __name__ == '__main__':

    cb = ConveyorBelt(
        name='cb',
        state=STATE,
        protocol=None,
        status=MOTOR_STA['OFF'],
        velocity=MOTOR_VEL['MIN']
    )
