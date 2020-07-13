# Ein Parser der über die Liste an Elementen läuft und abprüft welche Verbindungen miteinander kommunizieren
# Anordnung der Elemente der Liste: [time, proto, eth_dst, eth_src, ip_src, ip_dst, tcp_src_port, tcp_dst_port]

from getCount import getCount

list_Con_Arp = []
list_Con_Arp_src = []
list_Con_Arp_dst = []
list_Con_TCP = []
list_Con_TCP_src = []
list_Con_TCP_dst = []
list_Con = []
list_Con_end = []


def parseCon(list):
    for e in list:
        if str(e[1]) == "ARP":
            if e[3] in list_Con_Arp_src:
                if e[2] in list_Con_Arp_dst:
                    continue
                else:
                    list_Con_Arp_dst.append(e[2])
                    list_Con_Arp.append(e)
            else:
                if e[2] in list_Con_Arp_dst:
                    list_Con_Arp_src.append(e[3])
                    list_Con_Arp.append(e)
                else:
                    list_Con_Arp_dst.append(e[2])
                    list_Con_Arp_src.append(e[3])
                    list_Con_Arp.append(e)
        # Prüft ein TCP Paket ab, und falls zwei IP Adressen über dieselbe Arp Adresse verfügen wird die zusätzliche IP Adresse hinten angefügt
        elif str(e[1]) == "TCP":
            if e[3] in list_Con_TCP_src:
                if e[2] in list_Con_TCP_dst:
                    for i in list_Con_TCP:
                        if (str(e[3]) == str(i[3])) and (str(e[2]) == str(i[2])):
                            if str(e[4]) != str(i[4]):
                                i.append(e[4])
                            elif str(e[5]) != str(i[5]):
                                i.append(e[5])
                            else:
                                continue
                        else:
                            continue
                else:
                    list_Con_TCP_dst.append(e[2])
                    list_Con_TCP.append(e)
            else:
                if e[2] in list_Con_TCP_dst:
                    list_Con_TCP_src.append(e[3])
                    list_Con_TCP.append(e)
                else:
                    list_Con_TCP_dst.append(e[2])
                    list_Con_TCP_src.append(e[3])
                    list_Con_TCP.append(e)

    for d in list_Con_Arp:
        list_Con.append(d)
    for f in list_Con_TCP:
        list_Con.append(f)

    length = len(list_Con)

    def getCon():
        for i in range(0, length):
            counter = getCount(list_Con[i][3], list_Con[i][2], list)
            list_Con[i].append(counter)
        return list_Con

    list_Con_end = getCon()

    return list_Con_end
