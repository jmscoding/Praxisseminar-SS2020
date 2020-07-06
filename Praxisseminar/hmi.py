"""
IN BEARBEITUNG

Zuletzt 06.07. : Hinzufuegen von HMI Protokolldaten

Praxisseminar hmi.py
"""

from minicps.devices import HMI
from utils import Praxisseminar_test_logger
from utils import STATE, HMI_DATA, PLC1_ADDR, HMI_TAGS, IP

import get_ip
import get_mac

#import sys
import time


HMI_ADDR = get_ip.get_ip()

HMI_MAC = get_mac.get_mac()

HMI_SERVER = {
    'address': HMI_ADDR,
    'tags': HMI_TAGS
}
HMI_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': HMI_SERVER
}

# constant tag addresses
SENSOR_1 = ('SENSOR', 1)
MOTOR_1 = ('MOTOR', 1)


class PHMI(HMI):

    """Praxisseminar HMI.

    HMI provides:
        - state APIs: e.g., get a water level indicator
        - network APIs: e.g., monitors a PLC's tag
    """


    def main_loop(self, sleep=10):
        """HMI main loop.

        :param float sleep: second[s] to sleep after each iteration
        """

        # die HMI Addresse zurueckgeben
        print 'DEBUG: die Adresse des aktuellen HMI lautet: ' + HMI_ADDR
        Praxisseminar_test_logger.debug('DEBUG: die Adresse des aktuellen HMI lautet: ' + HMI_ADDR)

        sec = 0
        while(True):

            rec_s11 = self.receive(SENSOR_1, PLC1_ADDR)
            self.send(SENSOR_1, rec_s11, HMI_ADDR)
            rec_m11 = self.receive(MOTOR_1, PLC1_ADDR)
            self.send(MOTOR_1, rec_m11, HMI_ADDR)
            Praxisseminar_test_logger.debug('Sensor_1: ' + rec_s11)
            Praxisseminar_test_logger.debug('Motor_1: ' + rec_m11)



            print "Sie haben folgende Optionen: "
            print
            eingabe = str(input("Auslesen Status: Taste 1/ Geschwindigkeit einstellen: Taste 2/ Ein-/Ausschalten: Taste 3/ Programm beenden: Taste 99 "))

            # evtl doch auf switch ... case umsteigen - geht nicht so wie ich mir das vorstelle

            # Status abfragen (Ein
            if eingabe == '1':
                motor = self.receive(MOTOR_1, PLC1_ADDR)
                self.send(MOTOR_1, motor, HMI_ADDR)
                print "DEBUG plc1 erhaelt motor: " + motor
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)

                # wenn mit eigenem Status-Bereich gearbeitet wird
                #self.send(MOTOR_1, motor, HMI_ADDR)

                if motor == 1:
                    print 'DEBUG plc1 motor: An'
                elif motor == 0:
                    print 'DEBUG plc1 motor: Aus'
                print
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)

            elif eingabe == '2':
                motor = self.receive(MOTOR_1, PLC1_ADDR)
                self.send(MOTOR_1, motor, HMI_ADDR)
                print "DEBUG plc1 erhaelt motor: " + motor
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)

                # siehe Eingabe '1'

                if motor == 1:
                    sensor = float(self.receive(SENSOR_1, PLC1_ADDR))
                    self.send(SENSOR_1, sensor, HMI_ADDR)
                    print 'DEBUG plc1 motor: An mit der Geschwindigkeit' + str(sensor)
                    Praxisseminar_test_logger.debug('Sensor_1: ' + str(sensor))

                    # Wollen Sie die Geschwindigkeit veraendern? Wie hoch soll die Geschwindigkeit sein (Rahmen der Geschwindigkeit anpassen)
                    change = input("Wollen Sie die Geschwindigkeit veraendern? J/N")

                    if change == "J" or change == "j":
                        new_vel = float(input("Geben Sie die neue Geschwindigkeit ein: "))
                        self.set(SENSOR_1, new_vel)
                        self.send(SENSOR_1, new_vel, PLC1_ADDR)
                        self.send(SENSOR_1, new_vel, HMI_ADDR)
                        print 'DEBUG plc1 motor: An mit neuer Geschwindigkeit' + str(new_vel)
                        Praxisseminar_test_logger.debug('Sensor_1: ' + str(new_vel))

                    elif change == "N" or change == "n":
                        break

                elif motor == 0:
                    print 'DEBUG plc1 motor: Aus'
                print
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)

            elif eingabe == '3':
                motor = self.receive(MOTOR_1, PLC1_ADDR)
                self.send(MOTOR_1, motor, HMI_ADDR)
                print "DEBUG plc1 erhaelt motor: " + motor
                Praxisseminar_test_logger.debug('Motor_1: ' + motor)

                if motor == 1:
                    onoff = input("Wollen Sie den Motor aus oder einschalten? Aus = 0 /Ein = 1")

                    if onoff == 0:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)
                        self.send(MOTOR_1, onoff, HMI_ADDR)
                    elif onoff == 1:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)
                        self.send(MOTOR_1, onoff, HMI_ADDR)

                elif motor == 0:
                    onoff = input("Wollen Sie den Motor aus oder einschalten? Aus = 0 /Ein = 1")

                    if onoff == 0:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)
                        self.send(MOTOR_1, onoff, HMI_ADDR)
                    elif onoff == 1:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)
                        self.send(MOTOR_1, onoff, HMI_ADDR)
            time.sleep(sleep)




if __name__ == "__main__":

    # notice that memory init is different form disk init
    phmi = PHMI(
        name='phmi',
        state=STATE,
        protocol=HMI_PROTOCOL,
        memory=HMI_DATA,
        disk=HMI_DATA)
