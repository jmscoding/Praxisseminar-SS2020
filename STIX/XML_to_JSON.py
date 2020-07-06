#Converting Nmap xml scan reports to json

import json
import xmltodict


#xml-Datei einfuegen
f = open("DieXml.xml")
xml_content = f.read()
f.close()
print(json.dumps(xmltodict.parse(xml_content),ident= 4, sort_keys=True))

