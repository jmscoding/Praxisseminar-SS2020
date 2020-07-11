"""
IN BEARBEITUNG

Zuletzt 06.07. : Hinzufuegen von HMI Protokolldaten

Praxisseminar hmi.py
"""

from minicps.devices import HMI
from utils import Praxisseminar_test_logger
from utils import STATE, PLC1_ADDR

from utils import HMI_PROTOCOL, HMI_DATA, HMI_ADDR


import time


MOTOR = ('MOTOR', 1)
SENSOR = ('SENSOR', 1)


class PHMI(HMI):

    """Praxisseminar HMI.

    HMI:
        - Man kann die Daten des Motors von der PLC ablesen
        - Man kann die PLC bedienen (ein-/ausschalten + Geschwindigkeit veraendern)
    """

    def main_loop(self, sleep=10):
        """HMI main
        """

        while(True):
            Praxisseminar_test_logger.debug("Die HMI mit Adresse " + str(HMI_ADDR) + " befindet sich in der main loop")
            print "Sie haben folgende Optionen: "
            print

            eingabe = int(raw_input("Auslesen Status: Taste 1/ Geschwindigkeit einstellen: Taste 2/ Ein-/Ausschalten: Taste 3/ Programm beenden: Taste 99 "))
            print 'DEBUG: eingabe = %s' % eingabe
            Praxisseminar_test_logger.debug("Der User hat folgendes eingegeben: %s" % str(eingabe))

            # Status abfragen
            if eingabe == 1:
                Praxisseminar_test_logger.debug("User befindet sich in der ersten if-Abfrage")
                motor = self.receive(MOTOR, PLC1_ADDR)
                print "DEBUG plc1 erhaelt motor: " + motor
                Praxisseminar_test_logger.info('Motor erhaelt von PLC1_ADDR: ' + motor)

                if motor == '1':
                    print 'DEBUG plc1 motor: An'
                    Praxisseminar_test_logger.info("Der Motor ist An")
                elif motor == '0':
                    print 'DEBUG plc1 motor: Aus'
                    Praxisseminar_test_logger.info("Der Motor ist Aus")

            # Geschwindigkeit einstellen
            elif eingabe == 2:
                Praxisseminar_test_logger.debug("User befindet sich in der zweiten if-Abfrage")
                motor = self.receive(MOTOR, PLC1_ADDR)
                print "DEBUG plc1 erhaelt motor: " + motor
                Praxisseminar_test_logger.info('Motor erhaelt von PLC1_ADDR: ' + motor)

                # siehe Eingabe '1'

                if motor == '1':
                    Praxisseminar_test_logger.info("Der Motor ist an")
                    sensor = self.receive(SENSOR, PLC1_ADDR)
                    print 'DEBUG plc1 motor: An mit der Geschwindigkeit' + sensor
                    Praxisseminar_test_logger.info('Sensor erhaelt von PLC1_ADDR: ' + sensor)

                    # Wollen Sie die Geschwindigkeit veraendern? Wie hoch soll die Geschwindigkeit sein (Rahmen der Geschwindigkeit anpassen)
                    change = raw_input("Wollen Sie die Geschwindigkeit veraendern? J/N")
                    Praxisseminar_test_logger.debug("Der User hat folgendes eingegeben: %s" % change)

                    if change == "J" or change == "j":
                        new_vel = float(raw_input("Geben Sie die neue Geschwindigkeit ein: "))
                        Praxisseminar_test_logger.debug("Der User hat folgendes eingegeben: %s" % str(new_vel))
                        self.send(SENSOR, new_vel, PLC1_ADDR)
                        print 'DEBUG plc1 motor: An mit neuer Geschwindigkeit' + str(new_vel)
                        Praxisseminar_test_logger.info('HMI sendet folgende SENSOR-Daten an PLC1_ADDR: ' + str(new_vel))

                    elif change == "N" or change == "n":
                        Praxisseminar_test_logger.debug("Elif-Abfrage wurde erreicht weil User ein N/n eingegeben hat")
                        continue

                elif motor == '0':
                    print 'DEBUG plc1 motor: Aus'
                    Praxisseminar_test_logger.info("Der Motor ist aus")
                print

            # Ein oder ausschalten
            elif eingabe == 3:
                Praxisseminar_test_logger.debug("User befindet sich in der dritten if-Abfrage")
                motor = self.receive(MOTOR, PLC1_ADDR)
                print "DEBUG plc1 erhaelt motor: " + motor
                Praxisseminar_test_logger.debug('Motor erhaelt von PLC1_ADDR: ' + motor)

                if motor == '1':
                    Praxisseminar_test_logger.info("Der Motor ist an")
                    onoff = int(raw_input("Wollen Sie den Motor auschalten? Bitte geben Sie 0 ein ansonsten 1"))
                    Praxisseminar_test_logger.debug("Der User hat folgendes eingegeben: %s" % str(onoff))

                    if onoff == 0:
                        self.send(MOTOR, onoff, PLC1_ADDR)
                        Praxisseminar_test_logger.info('HMI sendet folgende MOTOR-Daten an PLC1_ADDR: ' + str(onoff))
                        self.send(SENSOR, 0.0, PLC1_ADDR)
                        Praxisseminar_test_logger.info('HMI sendet folgende SENSOR-Daten an PLC1_ADDR: ' + str(0.0))
                        Praxisseminar_test_logger.debug('Da der Motor ausgeschaltet wurde wird die Geschwindigkeit des Foerderbandes auf 0.0 zurueckgesetzt')


                    elif onoff == 1:
                        self.send(MOTOR, onoff, PLC1_ADDR)
                        Praxisseminar_test_logger.info('HMI sendet folgende MOTOR-Daten an PLC1_ADDR: ' + str(onoff))

                elif motor == '0':
                    Praxisseminar_test_logger.info("Der Motor ist aus")
                    onoff = int(raw_input("Wollen Sie den Motor einschalten? Bitte geben Sie 1 ein ansonsten 0"))
                    Praxisseminar_test_logger.debug("Der User hat folgendes eingegeben: %s" % str(onoff))

                    if onoff == 0:
                        self.send(MOTOR, onoff, PLC1_ADDR)
                        Praxisseminar_test_logger.info('HMI sendet folgende MOTOR-Daten an PLC1_ADDR: ' + str(onoff))

                    elif onoff == 1:
                        self.send(MOTOR, onoff, PLC1_ADDR)
                        Praxisseminar_test_logger.info('HMI sendet folgende MOTOR-Daten an PLC1_ADDR: ' + str(onoff))


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
