"""
Praxisseminar run.py
"""

from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS
from topo import CbTopo

import sys


class PraxisseminarCPS(MiniCPS):

    """Main container used to run the simulation."""

    def __init__(self, name, net):

        self.name = name
        self.net = net

        self.net.start()

        # start devices
        # plc1 = self.net.get('plc1')
        # plc1.cmd(sys.executable + ' plc1.py &')

        CLI(self.net)

        self.net.stop()

if __name__ == "__main__":

    topo = CbTopo()
    net = Mininet(topo=topo)

    Praxisseminarcps = PraxisseminarCPS(
        name='PraxisseminarCPS',
        net=net)