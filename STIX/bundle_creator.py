# erstellt ein Bundle eines Stix Vorfalls

from stix2.v21 import (ThreatActor, Identity, Relationship, Bundle, AttackPattern, ExternalReference, Infrastructure, Tool, Vulnerability, IPv4Address, MACAddress, NetworkTraffic)
from json_parser import getCon, getTime
import uuid


# Bekommt den ersten Zeitstempel aus dem JSON-File
time = getTime()
conList = getCon()

# Die SDOs
threat_actor = ThreatActor(
    id="threat-actor--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Innentaeter",
    description="Ein Innentaeter versucht den aktiven Prozess mitzuhoeren, Informationen zu gewinnen und Daten zu manipulieren.",
    threat_actor_types=["insider-disgruntled"],
    aliases=["Verraeter"],
    roles=["agent"],
    goals=["Informationen ueber den Netzwerkverkehr im Unternehmen gewinnen", "Daten manipulieren"],
    sophistication="expert",
    resource_level="organization",
    primary_motivation="personal-gain",
    secondary_motivation=["dominance"]
)

infrastructure1 = Infrastructure(
    id="infrastructure--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Netzwerk - Firma A",
    description="Das Netzwerk der Firma A, welches aus mehreren Teilnehmern besteht"
)


identity1 = Identity( # Angreifer-Firma
    id="identity--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Firma B",
    description="Firma B versucht Innentaeter anzuwerben und dadurch der Konkurrenz zu schaden.",
    identity_class="organization"
    #contact_information="disco-team@stealthemail.com"
)

identity2 = Identity( # Firma die angegriffen wird
    type="identity",
    id="identity--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Firma A",
    description="Firma A ist die angegriffene Firma.",
    identity_class="organization"
)

ref_capec1 = ExternalReference(
    source_name="capec",
    url="https://capec.mitre.org/data/definitions/94.html",
    external_id="CAPEC-94"
)

ref_capec2 = ExternalReference(
    source_name="capec",
    url="https://capec.mitre.org/data/definitions/343.html",
    external_id="CAPEC-343"
)

attack_pattern1 = AttackPattern(
    type="attack-pattern",
    id="attack-pattern--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Man in the Middle Attack",
    external_references=[ref_capec1]
)

attack_pattern2 = AttackPattern(
    type="attack-pattern",
    id="attack-pattern--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="DOS-Attack",
    external_references=[ref_capec2]
)

tool1 = Tool(
    type="tool",
    id="tool--" + str(uuid.uuid4()),
    created=time,
    modfied=time,
    name="Ettercap",
    description="Ermöglicht einem Angreifer ARP-Poisoning"
)

tool2 = Tool(
    type="tool",
    id="tool--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Wireshark",
    description="Ermöglicht dem Angreifer das Aufzeichnen von Netzwerkverkehr"
)

tool3 = Tool(
    type="tool",
    id="tool--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="hping3",
    description="Programm, dass mittels IP-Spoofing und einer DOS-Attacke den Netzwerkverkehr eines Hosts stört"
)

tool4 = Tool(
    type="tool",
    id="tool--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="HMI",
    description="Programm, dass den Status eines physischen Vorgangs lesen und verändern kann"
)

vulnerability1 = Vulnerability(
    type="vulnerability",
    id="vulnerability--" + str(uuid.uuid4()),
    created=time,
    modified=time,
    name="Förderband",
    description="Der Netzwerkverkehr zwischen einer HMI und einem PLC, der ein Förderband steuert"
)

# Die SCOs
# Hinzufügen der IP-Adressen und MAC-Adressen -- Vorab Prüfung wie viele Verbindungen existieren
"""
ipv4address1 = IPv4Address(
    type="ipv4-addr",
    id="ipv4-addr--" + str(uuid.uuid4()),
    value="Listenelement"
    resolves_to_refs=["MAC"]
)

macaddress1 = MACAddress(
    type="mac-addr",
    id="mac-addr--" + str(uuid.uuid4()),
    value="Listenelement"   
)

networktraffic1 = NetworkTraffic(
    type="network-traffic",
    id="network-traffic--" + str(uuid.uuid4()),
)

"""


# Alle Beziehungstypen hinzufügen
# Die SROs
relationship1 = Relationship(threat_actor, 'attributed-to', identity1)
relationship2 = Relationship(threat_actor, 'attributed-to', identity2)
relationship3 = Relationship(threat_actor, 'uses', attack_pattern1)
relationship4 = Relationship(threat_actor, 'uses', attack_pattern2)

# Das Bundle
bundle = Bundle(objects=[attack_pattern1, attack_pattern2, threat_actor, identity1, identity2, infrastructure1, relationship1, relationship2, relationship3, tool1, tool2, ])
