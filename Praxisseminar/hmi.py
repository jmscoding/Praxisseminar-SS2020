"""
IN BEARBEITUNG

Praxisseminar hmi.py
"""

from minicps.devices import HMI
from utils import Praxisseminar_test_logger
from utils import STATE, PLC1_DATA, PLC1_PROTOCOL, PLC1_ADDR

import get_ip

import sys
import time


HMI_ADDR = get_ip()

# constant tag addresses
SENSOR_1 = ('SENSOR', 1)
MOTOR_1 = ('MOTOR', 1)


class PHMI(HMI):

    """Praxisseminar HMI.

    HMI provides:
        - state APIs: e.g., get a water level indicator
        - network APIs: e.g., monitors a PLC's tag
    """


    def main_loop(self, sleep=0.5):
        """HMI main loop.

        :param float sleep: second[s] to sleep after each iteration
        """

        # die HMI Addresse zurückgeben
        print 'DEBUG: die Adresse des aktuellen HMI lautet: ' + HMI_ADDR
        Praxisseminar_test_logger.debug('DEBUG: die Adresse des aktuellen HMI lautet: ' + HMI_ADDR)

        sec = 0
        while(sec < 1):

            rec_s11 = self.receive(SENSOR_1, PLC1_ADDR)
            rec_m11 = self.receive(MOTOR_1, PLC1_ADDR)
            Praxisseminar_test_logger.debug('Sensor_1: ' + rec_s11)
            Praxisseminar_test_logger.debug('Motor_1: ' + rec_m11)



            print "Sie haben folgende Optionen: "
            print
            eingabe = str(input("Auslesen Status: Taste 1/ Geschwindigkeit einstellen: Taste 2/ Ein-/Ausschalten: Taste 3/ Programm beenden: Taste 99 "))

            if eingabe == '1':
                motor = self.get(MOTOR_1)
                if motor == 1:
                    print 'DEBUG plc1 motor: An'
                elif motor == 0:
                    print 'DEBUG plc1 motor: Aus'
                print
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)

            elif eingabe == '2':
                motor = self.get(MOTOR_1)
                if motor == 1:
                    sensor = self.get(SENSOR_1)
                    print 'DEBUG plc1 motor: An mit der Geschwindigkeit' + sensor

                elif motor == 0:
                    print 'DEBUG plc1 motor: Aus'
                print
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)


            print "TODO HMI main_loop: please override me"
            time.sleep(sleep)

            sec += 1



if __name__ == "__main__":

    # notice that memory init is different form disk init
    phmi = PHMI(
        name='phmi',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)
