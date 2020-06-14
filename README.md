# Praxisseminar-SS2020
Praxisseminar im SS2020 im Studiengang Master of Science 

Angriffssimulation und strukturierte Datenerfassung

Der Digitale Zwilling kann mittels seines Simulationsmodus strukturierte Daten für Cyber Threat Intelligence (CTI) liefern. Mittels Simulationen anhand von Mininet, Mininet-Wifi, MiniCPS oder ähnlichem soll ein realistisches Industriesetting (z.B. eine Wasseraufbereitungsanlage) abgebildet werden. Für das Praxisseminar soll daraufhin ein Angriff simuliert und der angefallene Netzwerkverkehr mitgeschnitten werden. Zuletzt sollen die so erfassten Daten strukturiert für CTI aufgearbeitet werden.


Szenario Kurzfassung:

Ein Hersteller für Abfüllanlagen will die Cybersicherheit seiner neuen Produktlinie überprüfen. Das Produkt besteht aus einem Fließband, welches durch einen Host (durch ein HMI) im Firmennetz gesteuert werden kann. Das Fließband wird durch einen Sensor überwacht. Die Werte des Sensors können von der HMI eingesehen werden. Zusätzlich verfügt das Fließband über ein Steuergerät, welches die Geschwindigkeit des Fließbandes regelt. Dieses Gerät kann von der HMI aus erreicht werden und durch einen PLC verändert werden (Geschwindigkeit erhöht oder verringert). 

Ein mögliches Angriffsszenario wäre ein Innentäter (als Threat Actor), der durch Bestechung von Konkurrenten oder Ähnliches dem Hersteller für Abfüllanlagen schaden möchte. Dazu gelingt es ihm eine verdeckte Datei im System des neuen Produktes einzuschleusen, die es einem Angreifer ermöglicht sich über einen Remotezugriff am Netzwerk des Fließbandes anzumelden. Der „Threat Actor“ versucht infolgedessen einen MITM-Angriff, um das Fließband zum Ausfall zu bringen indem er die Geschwindigkeit des Bandes verändert.
