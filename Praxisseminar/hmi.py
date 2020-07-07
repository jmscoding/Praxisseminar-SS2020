"""
IN BEARBEITUNG

Zuletzt 06.07. : Hinzufuegen von HMI Protokolldaten

Praxisseminar hmi.py
"""

from minicps.devices import HMI
from utils import Praxisseminar_test_logger
from utils import STATE, HMI_DATA, PLC1_ADDR, HMI_TAGS

import get_ip
import get_mac

#import sys
import time


HMI_ADDR = get_ip.get_ip()

HMI_MAC = get_mac.get_mac(HMI_ADDR)

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
# senden an PLC1
SENSOR_1 = ('SENSOR', 2)
MOTOR_1 = ('MOTOR', 2)
# lesen von PLC1
MOTOR = ('MOTOR', 1)
SENSOR = ('SENSOR', 1)

class PHMI(HMI):

    """Praxisseminar HMI.

    HMI provides:
        - state APIs: e.g., get a water level indicator
        - network APIs: e.g., monitors a PLC's tag
    """


    def main_loop(self, sleep=10):
        """HMI main loop.


        """

        # die HMI Addresse zurueckgeben
        print 'DEBUG: die Adresse des aktuellen HMI lautet: ' + HMI_ADDR + ' ' + str(HMI_MAC)
        Praxisseminar_test_logger.debug('DEBUG: die Adresse des aktuellen HMI lautet: ' + HMI_ADDR + ' ' + str(HMI_MAC))

        while(True):

            rec_s11 = float(self.receive(SENSOR, PLC1_ADDR))
            print 'DEBUG: SENSOR ' + str(rec_s11)
            self.send(SENSOR_1, rec_s11, HMI_ADDR)
            rec_m11 = int(self.receive(MOTOR, PLC1_ADDR))
            print 'DEBUG: MOTOR ' + str(rec_m11)
            self.send(MOTOR_1, rec_m11, HMI_ADDR)
            Praxisseminar_test_logger.debug('Sensor_1: ' + str(rec_s11))
            Praxisseminar_test_logger.debug('Motor_1: ' + str(rec_m11))



            print "Sie haben folgende Optionen: "
            print
            eingabe = int(raw_input("Auslesen Status: Taste 1/ Geschwindigkeit einstellen: Taste 2/ Ein-/Ausschalten: Taste 3/ Programm beenden: Taste 99 "))
            print 'DEBUG: eingabe = %s' % eingabe
            # evtl doch auf switch ... case umsteigen - geht nicht so wie ich mir das vorstelle

            # Status abfragen
            if eingabe == 1:
                motor = int(self.receive(MOTOR_1, HMI_ADDR))
                print "DEBUG plc1 erhaelt motor: " + str(motor)
                Praxisseminar_test_logger.debug('Motor_1: ' + str(motor))

                # wenn mit eigenem Status-Bereich gearbeitet wird


                if motor == 1:
                    print 'DEBUG plc1 motor: An'
                elif motor == 0:
                    print 'DEBUG plc1 motor: Aus'


            #Geschwindigkeit einstellen
            elif eingabe == 2:
                motor = int(self.receive(MOTOR_1, HMI_ADDR))
                print "DEBUG plc1 erhaelt motor: " + str(motor)
                Praxisseminar_test_logger.debug('Motor_1: ' + str(motor))

                # siehe Eingabe '1'

                if motor == 1:
                    sensor = float(self.receive(SENSOR_1, HMI_ADDR))
                    print 'DEBUG plc1 motor: An mit der Geschwindigkeit' + str(sensor)
                    Praxisseminar_test_logger.debug('Sensor_1: ' + str(sensor))

                    # Wollen Sie die Geschwindigkeit veraendern? Wie hoch soll die Geschwindigkeit sein (Rahmen der Geschwindigkeit anpassen)
                    change = raw_input("Wollen Sie die Geschwindigkeit veraendern? J/N")

                    if change == "J" or change == "j":
                        new_vel = float(raw_input("Geben Sie die neue Geschwindigkeit ein: "))
                        self.send(SENSOR_1, new_vel, PLC1_ADDR)
                        print 'DEBUG plc1 motor: An mit neuer Geschwindigkeit' + str(new_vel)
                        Praxisseminar_test_logger.debug('Sensor_1: ' + str(new_vel))

                    elif change == "N" or change == "n":
                        continue

                elif motor == 0:
                    print 'DEBUG plc1 motor: Aus'
                print
                Praxisseminar_test_logger.debug('Motor_1: ' + str(motor))

            #Ein oder ausschalten
            elif eingabe == 3:
                motor = int(self.receive(MOTOR_1, PLC1_ADDR))
                print "DEBUG plc1 erhaelt motor: " + str(motor)
                Praxisseminar_test_logger.debug('Motor_1: ' + str(motor))

                if motor == 1:
                    onoff = int(raw_input("Wollen Sie den Motor aus oder einschalten? Aus = 0 /Ein = 1"))

                    if onoff == 0:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)

                    elif onoff == 1:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)


                elif motor == 0:
                    onoff = int(raw_input("Wollen Sie den Motor aus oder einschalten? Aus = 0 /Ein = 1"))

                    if onoff == 0:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)

                    elif onoff == 1:
                        self.send(MOTOR_1, onoff, PLC1_ADDR)


            elif eingabe == 99:
                print 'DEBUG: HMI Shutdown'
                Praxisseminar_test_logger.debug('DEBUG: HMI Shutdown')
                break

            time.sleep(sleep)




if __name__ == "__main__":

    # notice that memory init is different form disk init
    phmi = PHMI(
        name='phmi',
        state=STATE,
        protocol=HMI_PROTOCOL,
        memory=HMI_DATA,
        disk=HMI_DATA)
