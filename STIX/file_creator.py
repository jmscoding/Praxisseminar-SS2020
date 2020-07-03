# erstellt eine Datei

import json
import bundle_creator

file = open('test.json', 'w')
file.write(json.dumps(bundle_creator.bundle))
file.close()

