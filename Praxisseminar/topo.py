"""
IN BEARBEITUNG

Praxisseminar conveyor belt (short CB, Fliessband) topology
"""

from mininet.topo import Topo

from utils import IP, MAC, NETMASK


class CbTopo(Topo):

    """Fliessband 1 plc + 1 Host mit HMI + 1 Angreifer + 1 Switch"""

    def build(self):

        switch = self.addSwitch('s1')

        plc1 = self.addHost(
            'plc1',
            ip=IP['plc1'] + NETMASK,
            mac=MAC['plc1'])
        self.addLink(plc1, switch)

        host1 = self.addHost(
            'host1',
            ip=IP['host1'] + NETMASK,
            mac=MAC['host1'])
        self.addLink(host1, switch)

        attacker = self.addHost(
            'attacker',
            ip=IP['attacker'] + NETMASK,
            mac=MAC['attacker'])
        self.addLink(attacker, switch)
