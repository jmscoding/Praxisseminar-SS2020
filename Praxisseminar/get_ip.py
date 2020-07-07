#gibt Ip Adresse des Hosts an

from netifaces import interfaces, ifaddresses, AF_INET
from utils import PLC1_ADDR

def get_ip():
    for ifaceName in interfaces():

        # Urspruenglicher Code
        #addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        #print '%s: %s' % (ifaceName, ', '.join(addresses))
        #print ifaceName

        #addresses = int([i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, ['No IP addr'])])
        #print addresses
        #return addresses

        for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}]):

            #print i['addr']
            if (i['addr'] != '127.0.0.1') or (i['addr'] != PLC1_ADDR):
                return str(i['addr'])

    return 0




#Funktionen zum Testen des Codes

#ip = get_ip()
#ip1 = str(ip)


#print ip1

