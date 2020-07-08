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

        time.sleep(sleep)

    def main_loop(self, sleep=10):
        print 'DEBUG: Praxisseminar plc1 enters main_loop'
        print

        count = 0
        END = 1000
        while(True):

            # Lese von HMI - vorher abpruefen ob HMI vorhanden


            rec_m11 = int(self.receive(MOTOR, PLC1_ADDR))
            self.send(MOTOR, rec_m11, PLC1_ADDR)

            print 'DEBUG: Sende %s an PLC1' % str(rec_m11)

            rec_s11 = float(self.receive(SENSOR, PLC1_ADDR))
            self.send(SENSOR, rec_s11, PLC1_ADDR)

            print 'DEBUG: Sende %s an PLC1' % str(rec_s11)

            time.sleep(sleep)
            count += 1

            # Programmabbruch bei zu hoher Geschwindigkeit

            if (count > END) or (rec_s11 > MOTOR_VEL['MAX']):
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
