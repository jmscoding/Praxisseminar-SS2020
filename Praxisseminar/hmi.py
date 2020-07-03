"""
IN BEARBEITUNG

Praxisseminar hmi.py
"""

from minicps.devices import HMI

from utils import STATE, PLC1_DATA, PLC1_PROTOCOL


import sys
import time


class PHMI(HMI):

    """Praxisseminar HMI.

    HMI provides:
        - state APIs: e.g., get a water level indicator
        - network APIs: e.g., monitors a PLC's tag
    """

    def _start(self):

        self.main_loop()

    def _stop(self):

        if self.protocol['mode'] > 0:
            self._protocol._server_subprocess.kill()

    def main_loop(self, sleep=0.5):
        """HMI main loop.

        :param float sleep: second[s] to sleep after each iteration
        """

        sec = 0
        while(sec < 1):

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
