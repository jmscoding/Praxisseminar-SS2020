"""
Praxisseminar plc1.py
"""

from minicps.devices import PLC
from utils import PLC1_DATA, STATE
from utils import PLC1_PROTOCOL, PLC1_ADDR
from utils import Praxisseminar_test_logger
from utils import MOTOR_VEL

import time


# constant tag addresses
SENSOR = ('SENSOR', 1)
MOTOR = ('MOTOR', 1)


# Die Klasse des Fliessbandes
class CbPLC1(PLC):

    def pre_loop(self, sleep=0.1):
        print 'DEBUG: Praxisseminar plc1 enters pre_loop'
        print
        self.get(MOTOR)
        self.get(SENSOR)

        time.sleep(sleep)

    def main_loop(self, sleep=10):
        print 'DEBUG: Praxisseminar plc1 enters main_loop'
        print

        while True:

            rec_m11 = int(self.receive(MOTOR, PLC1_ADDR))
            self.set(MOTOR, rec_m11)
            Praxisseminar_test_logger.info("Motor erhaelt von PLC1_ADDR: %s" % str(rec_m11))
            self.send(MOTOR, rec_m11, PLC1_ADDR)
            Praxisseminar_test_logger.info("Motor sendet an PLC1_ADDR: %s" % str(rec_m11))
            print 'DEBUG: Sende %s an PLC1' % str(rec_m11)

            sensor = self.get(SENSOR)
            Praxisseminar_test_logger.info("Sensor: %s" % str(sensor))

            rec_s11 = float(self.receive(SENSOR, PLC1_ADDR))
            # Programmabbruch bei zu hoher Geschwindigkeit

            if rec_s11 > MOTOR_VEL['MAX']:
                print 'DEBUG Praxisseminar plc1 shutdown'
                Praxisseminar_test_logger.warning('PLC1 shutdown, die Geschwindigkeit hat das Maximum ueberschritten ')
                self.send(SENSOR, 0.0, PLC1_ADDR)
                self.set(SENSOR, 0.0)
                self.send(MOTOR, 0, PLC1_ADDR)
                self.set(MOTOR, 0.0)
                break


            Praxisseminar_test_logger.info("Motor erhaelt von PLC1_ADDR: %s" % str(rec_m11))
            Praxisseminar_test_logger.info("Sensor erhaelt von PLC1_ADDR: %s" % str(rec_s11))
            self.send(SENSOR, rec_s11, PLC1_ADDR)
            Praxisseminar_test_logger.info("Sensor sendet an PLC1_ADDR: %s" % str(rec_s11))
            self.set(SENSOR, rec_s11)
            Praxisseminar_test_logger.info("Sensor setzt : %s" % str(rec_s11))

            print 'DEBUG: Sende %s an PLC1' % str(rec_s11)

            time.sleep(sleep)


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc1 = CbPLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)
