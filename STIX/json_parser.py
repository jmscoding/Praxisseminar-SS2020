import json
from forTime import fortime
from parseCon import parseCon


# Konstanten fuer die Abfrage
TCP_PROTO = 'eth:ethertype:ip:tcp'
ARP_PROTO = 'eth:ethertype:arp'

liste = []
liste_con = []
liste_src = []
liste_dst = []
liste_src_mac = []
liste_dst_mac = []
i = 0

# File 1 funktioniert nicht wegen eines DecodeErrors - File 2 funktioniert
# file 1: 'C:/Users/Johan/OneDrive/Desktop/Wirtschaftsinformatik/2. Semester/05 Praxisseminar/STIX/angriff_dos.json'
# file 2: 'C:/Users/Johan/OneDrive/Desktop/Wirtschaftsinformatik/2. Semester/05 Praxisseminar/STIX/angriff_MITM.json'

# Lese ein JSON File
with open("C:/Users/Johan/OneDrive/Desktop/Wirtschaftsinformatik/2. Semester/05 Praxisseminar/STIX/angriff_MITM.json", "r") as f:
    data = json.load(f)

for d in data:
    protocol = d['_source']['layers']['frame']['frame.protocols']

    if TCP_PROTO in protocol:
        proto = 'TCP'
        time = fortime(d['_source']['layers']['frame']['frame.time'])
        eth_dst = d['_source']['layers']['eth']['eth.dst']
        eth_src = d['_source']['layers']['eth']['eth.src']
        ip_src = d['_source']['layers']['ip']['ip.src']
        ip_dst = d['_source']['layers']['ip']['ip.dst']
        tcp_src_port = d['_source']['layers']['tcp']['tcp.srcport']
        tcp_dst_port = d['_source']['layers']['tcp']['tcp.dstport']

        # Daten in ein Liste schreiben
        liste.append([time, proto, eth_dst, eth_src, ip_src, ip_dst, tcp_src_port, tcp_dst_port])

    elif ARP_PROTO in protocol:
        proto = 'ARP'
        time = fortime(d['_source']['layers']['frame']['frame.time'])
        eth_dst = d['_source']['layers']['eth']['eth.dst']
        eth_src = d['_source']['layers']['eth']['eth.src']

        # Daten in ein Liste schreiben
        liste.append([time, proto, eth_dst, eth_src])

    else:
        continue

# Erstellt eine Liste mit allen IP und MAC Adressen jeweils als SRC und DST und speichert diese auch als Connection
# Funktion dafür besser
End_list = parseCon(liste)

print(len(liste))
print(End_list)

# Daten in eine Text-Datei schreiben, wie viele Pakete gab es insgesamt, 
file = open('test.txt', 'w')

file.write('Gesamtanzahl Pakete: ' + str(len(liste)))
file.write(str('\n'))

for l in End_list:
    file.write(str(l))
    file.write(str('\n'))
file.close()


def getTime():
    return liste[0][0]


"""
for element in liste:

    if element[1] == 'ARP':
        continue
    else:
        if str(element[3]) in liste_src_mac:
            if str(element[2]) in liste_dst_mac:
                continue
            else:
                liste_dst_mac.append(element[2])
                liste_dst.append([element[2], element[5]])
                liste_con.append([element[3], element[4], element[2], element[5]])
        else:
            if str(element[2]) in liste_dst:
                liste_src_mac.append(element[3])
                liste_src.append([element[3], element[4]])
                liste_con.append([element[3], element[4], element[2], element[5]])
            else:
                liste_src_mac.append(element[3])
                liste_dst_mac.append(element[2])
                liste_src.append([element[3], element[4]])  # Schema MAC IP
                liste_dst.append([element[2], element[5]])
                liste_con.append([element[3], element[4], element[2], element[5]])

# Welche Teilnehmer existieren und mit wem kommunizieren sie
# Print Statements zum Debuggen
print("MITM-Attacke:")
print("SRC_Liste_MAC: " +str(liste_src_mac))
print("DST_Liste_MAC: " +str(liste_dst_mac))
print("SRC_Liste_MAC_IP: " + str(liste_src))
print("DST_Liste_MAC_IP: " + str(liste_dst))
print("Liste_Connections: " + str(liste_con))
print("Anzahl Verbindungen: " +str(len(liste_con)))

# Wenn man bereits weiß welche Verbindungen bestehen kann abgeprüft werden wie oft die Verbindungen vorkommen

l = len(liste_con)

# Funktionen zum debuggen
counter_con_1 = getCount(liste_con[0][0], liste_con[0][2], liste)
counter_con_2 = getCount(liste_con[1][0], liste_con[1][2], liste)

print("Anzahl Auftreten Verbindung 1: " + str(counter_con_1))
print("Anzahl Auftreten Verbindung 2: " + str(counter_con_2))


def getTime():
    return liste[0][0]


# Daten in eine Text-Datei schreiben
file = open('Dateipfad', 'w')

for l in liste:
    if l[1] == 'TCP':
        file.write('Zeit: ' + l[0] + ' Protokoll: ' + l[1] + ' MAC_DST: ' + l[2] + ' MAC_SRC: ' + l[3] + ' IP_SRC: ' + l[4] + ' IP_DST: ' + l[5] + ' TCP_SRC_PORT: ' + l[6] + ' TCP_DST_PORT: ' + l[7] + '\n')
    elif l[1] == 'ARP':
        file.write('Zeit: ' + l[0] + ' Protokoll: ' + l[1] + ' MAC_DST: ' + l[2] + ' MAC_SRC: ' + l[3] + '\n')
    else:
        continue

file.close()
"""
