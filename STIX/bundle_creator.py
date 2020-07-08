# erstellt ein Bundle eines Stix Vorfalls

from stix2.v21 import (ThreatActor, Identity, Relationship, Bundle, AttackPattern, ExternalReference)

# automatische Uebernahme der Zeitangabe und wann es modifiziert wurde
# automatisches Hinzufuegen einer ID

# Fragen
# 1. muss id nach RFC 4122-complient UUID aufgebaut werden
#

threat_actor = ThreatActor(
    id="threat-actor--1",
    created="2020-07-08T23:39:03.893Z",
    modified="2020-07-08T23:39:03.893Z",
    name="Innentaeter",
    description="Ein Innentaeter versucht den aktiven Prozess mitzuhoeren, Informationen zu gewinnen und Daten zu manipulieren.",
    threat_actor_types=["insider-disgruntled"], #muss noch geaendert werden
    aliases=["Verraeter"], #muss noch geaendert werden
    roles=["agent"],
    goals=["Informationen ueber den Netzwerkverkehr im Unternehmen gewinnen", "Daten manipulieren"],
    sophistication="expert",
    resource_level="organization",
    primary_motivation="personal-gain"
)

identity1 = Identity( # Angreifer-Firma
    id="identity--1",
    created="2020-07-08T18:05:49.307Z",
    modified="2020-07-08T18:05:49.307Z",
    name="Firma B",
    description="Firma B versucht Innentaeter anzuwerben und dadurch der Konkurrenz zu schaden.",
    identity_class="organization"
    #contact_information="disco-team@stealthemail.com"
)

identity2 = Identity( # Firma die angegriffen wird
    type="identity",
    id="identity--2",
    created="2020-07-08T23:39:03.893Z",
    modified="2020-07-08T23:39:03.893Z",
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
    id="attack-pattern--1",
    created="2020-07-08T23:39:03.893Z",
    modified="2020-07-08T23:39:03.893Z",
    name="Man in the Middle Attack",
    external_references=[ref_capec1]
)

attack_pattern2 = AttackPattern(
    type="attack-pattern",
    id="attack-pattern--2",
    created="2020-07-08T23:39:03.893Z",
    modified="2020-07-08T23:39:03.893Z",
    name="DOS-Attack",
    external_references=[ref_capec2]
)

relationship1 = Relationship(threat_actor, 'attributed-to', identity1)
relationship2 = Relationship(threat_actor, 'attributed-to', identity2)
relationship3 = Relationship(threat_actor, 'uses', attack_pattern1)
relationship4 = Relationship(threat_actor, 'uses', attack_pattern2)

bundle = Bundle(objects=[attack_pattern1, attack_pattern2, threat_actor, identity1, identity2, relationship1, relationship2, relationship3])
