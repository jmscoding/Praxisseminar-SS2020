"""
Praxisseminar plc1.py
"""

from minicps.devices import PLC
from utils import PLC1_DATA, STATE, MOTOR_VEL
from utils import PLC1_PROTOCOL, PLC1_ADDR
from utils import Praxisseminar_test_logger

from hmi import HMI_ADDR

import time
# import os
# import sys

# constant tag addresses
SENSOR = ('SENSOR', 1)
MOTOR = ('MOTOR', 1)

# Verbindungen zwischen einer HMI und der PLC
# MOTOR_1 = ('MOTOR', 2)
# SENSOR_1 = ('SENSOR', 2)



# TODO: decide how to map what tuples into memory and disk
class CbPLC1(PLC):

    def pre_loop(self, sleep=0.1):
        print 'DEBUG: Praxisseminar plc1 enters pre_loop'
        print

        time.sleep(sleep)

    def main_loop(self, sleep=10):
        print 'DEBUG: Praxisseminar plc1 enters main_loop'
        print

        # self.set(MOTOR, 0)
        # self.set(SENSOR, MOTOR_VEL['MIN'])

        count = 0
        END = 1000
        while(True):

            '''
            get_s11 = float(self.get(SENSOR))
            print 'DEBUG: Praxisseminar plc1 receive SENSOR: ' + str(get_s11)
            self.send(SENSOR, get_s11, PLC1_ADDR)

            get_m11 = int(self.get(MOTOR))
            print 'DEBUG: Praxisseminar plc1 receive MOTOR: ' + str(get_m11)
            self.send(MOTOR, get_m11, PLC1_ADDR)
            '''

            print str(HMI_ADDR)

            # Lese von HMI - vorher abpruefen ob HMI vorhanden

            rec_m11 = int(self.receive(MOTOR, HMI_ADDR))
            self.send(MOTOR, rec_m11, PLC1_ADDR)

            print 'DEBUG: Sende %s an PLC1' % str(rec_m11)

            rec_s11 = float(self.receive(SENSOR, HMI_ADDR))
            self.send(MOTOR, rec_s11, PLC1_ADDR)

            print 'DEBUG: Sende %s an PLC1' % str(rec_s11)

            time.sleep(sleep)
            count += 1

            if count > END:
                print 'DEBUG Praxisseminar plc1 shutdown'
                Praxisseminar_test_logger.debug('PLC1 shutdown ')
                break


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc1 = CbPLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)
