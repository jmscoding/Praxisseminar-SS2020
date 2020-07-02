"""
IN BEARBEITUNG:
- physischer Prozess im End Effekt nur starten und beenden des Fliessbandes und Bestimmen der Geschwindigkeit des Motors


Fliessband physical process

"""


from minicps.devices import CB

from utils import LIT_101_M, RWT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

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

        # Standardmäßig ist der Motor des Foerderbandes an
        self.set(MOTOR, 1)
        # Praxisseminar STATE INIT)


    def main_loop(self):

        count = 0
        while(count == 1000):

            # überprüfe ob Motor an ist
            # wenn ja dann setze standarmäßig Anfangsgeschwindigkeit

            motor = self.get(MOTOR)
            if int(MOTOR) == 1:

                self.set(FIT101, PUMP_FLOWRATE_IN)
                inflow = PUMP_FLOWRATE_IN * PP_PERIOD_HOURS
                # print "DEBUG RawWaterTank inflow: ", inflow
                water_volume += inflow
            else:
                self.set(SENSOR, 0.00)

            # compute new water_level
            new_level = water_volume / self.section

            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            print "DEBUG new_level: %.5f \t delta: %.5f" % (
                new_level, new_level - self.level)
            self.level = self.set(LIT101, new_level)

            # 988 sec starting from 0.500 m
            if new_level >= LIT_101_M['HH']:
                print 'DEBUG RawWaterTank above HH count: ', count
                break

            # 367 sec starting from 0.500 m
            elif new_level <= LIT_101_M['LL']:
                print 'DEBUG RawWaterTank below LL count: ', count
                break

            count += 1
            time.sleep(PP_PERIOD_SEC)


if __name__ == '__main__':

    cb = ConveyorBelt(
        name='cb',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=RWT_INIT_LEVEL
    )
