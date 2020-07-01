"""
Praxisseminar plc1.py
"""

from minicps.devices import PLC
from utils import PLC1_DATA, STATE
from utils import PLC1_PROTOCOL, PLC1_ADDR
from utils import Praxisseminar_test_logger

import time
import os
import sys


# constant tag addresses
SENSOR1_1 = ('SENSOR1', 1)
ACTUATOR1_1 = ('ACTUATOR1', 1)



# TODO: decide how to map what tuples into memory and disk
class CbPLC1(PLC):

    def pre_loop(self, sleep=0.1):
        print 'DEBUG: Praxisseminar plc1 enters pre_loop'
        print
		

        # sensor1 = self.set(SENSOR1_1, 2)
        # print 'DEBUG: Praxisseminar plc1 sensor1: ', self.get(SENSOR1_1)
        # self.memory['SENSOR1'] = sensor1
        self.send(SENSOR1_1, 2, PLC1_ADDR)

        time.sleep(sleep)

    def main_loop(self, sleep=0.5):
        print 'DEBUG: Praxisseminar plc1 enters main_loop'
        print

        count = 0
        END = 6e6
        while(True):
            rec_s11 = self.receive(SENSOR1_1, PLC1_ADDR)
            # print 'DEBUG: toy plc1 receive SENSOR3_1: ', rec_s31
            get_s11 = self.get(SENSOR1_1)
            print 'DEBUG: Praxisseminar plc1 get SENSOR1_1: ', get_s11
			Praxisseminar_test_logger.DEBUG('Praxisseminar plc1 get SENSOR1_1: ' + str(get_s11)) 

            time.sleep(1)
            count += 1

            if count > END:
                print 'DEBUG Praxisseminar plc1 shutdown'
                break


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc1 = CbPLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)
		
